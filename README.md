# Grocery Product Recommendation Bot 🛒
This project is a capstone project that involves building a recommendation system for grocery products based on a dataset from BigBasket. The aim is to create a bot that helps users discover grocery items that align with their interests, improving user experience and product discovery in an e-commerce context.

### 📁 Dataset
Source: BigBasket Products CSV

Contents: Product names, categories, subcategories, brands, and descriptions

Usage: The data is used to train a recommendation model after thorough preprocessing and exploratory analysis.

### 🧹 Data Preprocessing
The preprocessing pipeline includes:

Handling missing values

Removing duplicates and irrelevant entries

Normalizing and encoding text data

Cleaning inconsistent formatting

Preprocessing enhances data quality and ensures optimal model performance.

### 📊 Exploratory Data Analysis (EDA)
The EDA process involves:

Analyzing product categories and subcategories

Distribution analysis of brands and prices

Visualizations using matplotlib and seaborn

Text frequency analysis on product names and descriptions

EDA helps to uncover patterns and trends, essential for feature selection and modeling.

### 🏗️ Feature Engineering
Text Vectorization: Used TF-IDF on product names and descriptions

Category Encoding: Transformed categorical variables

Dimensionality Reduction: Applied techniques like PCA (if used)

These features form the foundation of the recommendation engine.

### 🧠 Recommendation Model
The recommendation system leverages cosine similarity between product vectors generated from text features. Based on user input or a selected product, the bot suggests similar items.

### 💬 Output
Top N recommended grocery products with:

Product name

Brand

Category

### 🛠️ Technologies Used
Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn (for TF-IDF and similarity computation)

Jupyter Notebook

### 🚀 How to Run
Clone this repository

Ensure you have the required libraries installed:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn scikit-learn
Run the Jupyter Notebook:

bash
Copy
Edit
jupyter notebook
Load the dataset and follow the cells step-by-step.

### 📌 Future Work
Deploy the bot as a web application

Add collaborative filtering features

Integrate user feedback loop for personalized suggestions
