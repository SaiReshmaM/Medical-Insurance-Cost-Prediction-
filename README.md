# Medical-Insurance-Cost-Prediction
deploy link:
https://8972s7wngq7lpujylc4tdf.streamlit.app/
# Problem Statement:

What are the primary factors influencing medical expenses?
How accurate are machine learning models in predicting medical expenses?
In what ways can machine learning models enhance the efficiency and profitability of health insurance companies?

Features
Exploring the dataset
Converting Categorical values to Numerical
Data Visualization (Plots of feature vs feature)
Data Preparation
Prediction using Linear Regression
Prediction using Random Forest Regressor
# Technologies and Libraries Used
# Programming Language:
Python 

# Libraries and Tools:

NumPy – for numerical computations and array handling

Pandas – for data manipulation and preprocessing

Matplotlib & Seaborn – for data visualization

Scikit-learn (sklearn) – for:

Data splitting (train_test_split)

Feature encoding (LabelEncoder, OneHotEncoder if used)

Models (LinearRegression, RandomForestRegressor)

Evaluation metrics (r2_score, mean_absolute_error, mean_squared_error)

Jupyter Notebook – for writing, executing, and visualizing code step-by-step in an interactive way

# 📊 Dataset Overview
Dataset: Medical Insurance Cost Dataset

Source: Commonly found on Kaggle

Records: ~1,300

Features:

Feature	Description
age	Age of the individual
sex	Gender (male or female)
bmi	Body Mass Index
children	Number of children covered by insurance
smoker	Smoking status (yes or no)
region	Residential area (southeast, northwest, etc.)
charges	Target variable – medical insurance cost

🔁 Project Workflow
# Data Collection

Load the dataset using pandas.read_csv()

# Data Exploration

View basic statistics and types using .info() and .describe()

Check for missing values, outliers, and correlations

# Data Preprocessing

Encode categorical features (sex, smoker, region) using Label Encoding or One-Hot Encoding

Normalize or scale features if needed (not always required for tree models like Random Forest)

# Feature & Target Split

Separate features (X) and target variable (charges)

# Train-Test Split

Use train_test_split() to divide the data into training and testing sets (e.g., 80/20)

# Model Training

Train Linear Regression and Random Forest Regressor on the training data

# Model Evaluation

Evaluate both models using MAE, RMSE, and R² Score on test data

# Comparison & Conclusion

Compare models and select the best one (Random Forest usually performs better)

# Single Input Prediction

Use the trained model to predict the cost for new user data


# 📁 Dataset
The dataset used can be downloaded from (Kaggle) 
# 🔑 Results
Model gave 86% accuracy for Medical Insurance Amount Prediction using Random Forest Regressor
