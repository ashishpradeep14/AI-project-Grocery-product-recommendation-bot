from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import pickle

# Load the model and data
with open(r'C:\Users\USER\Downloads\sentence_transformer_model\sentence_transformer_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the dataframe with embeddings
dp = pd.read_pickle(r"C:\Users\USER\Downloads\sentence_transformer_model\products_with_embeddings.pkl")

app = FastAPI()
templates = Jinja2Templates(directory='C:\\Users\\USER\\Downloads\\sentence_transformer_model\\templates')

def recommend_products(user_input, dp, model, top_n=5):
    user_embedding = model.encode(user_input)
    dp['similarity'] = dp['embeddings'].apply(lambda x: util.pytorch_cos_sim(user_embedding, x).item())
    recommendations = dp.sort_values(by='similarity', ascending=False).head(top_n)
    return recommendations[['product','brand','category', 'description', 'sale_price', 'rating']]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index_1.html", {"request": request, "recommendations": []})

@app.post("/recommend", response_class=HTMLResponse)
async def get_recommendations(request: Request):
    form = await request.form()
    user_input = form.get("user_input")
    recommendations = recommend_products(user_input, dp, model)
    return templates.TemplateResponse("index_1.html", {
        "request": request, 
        "recommendations": recommendations.to_dict(orient='records')
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
