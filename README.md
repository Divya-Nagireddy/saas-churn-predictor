# 🚀 SaaS Saver: AI Customer Churn Predictor

## The Problem
Software companies lose millions of dollars a year to customer churn. By the time a user clicks "cancel subscription," it is too late to save them. 

## The Solution
I built a Machine Learning pipeline that predicts if a customer is a flight risk *before* they cancel. By analyzing user tenure, billing patterns, and account settings, this AI allows customer service teams to proactively offer discounts to high-risk users.

## 🛠️ The Tech Stack
* **Data Pipeline:** Python, Pandas, Scikit-Learn
* **AI Brain:** Random Forest Classifier (Trained on IBM Telco Dataset)
* **API Backend:** FastAPI, Uvicorn
* **Infrastructure:** Docker

## 🚀 How to Run this Locally (Docker)
You can spin this entire AI API up in seconds using Docker.

1. Clone this repository.
2. Build the image: `docker build -t saas-ai-api .`
3. Run the container: `docker run -p 8000:8000 saas-ai-api`
4. Go to `http://localhost:8000/docs` to test the live AI predictions!