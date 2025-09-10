# 🏠 House Price Prediction

This project predicts house prices using various regression models based on multiple features such as location, area, BHK, and more. The goal is to build an end-to-end ML pipeline for house price estimation using real-world housing data scraped from the web.

## 📊 Features

- **Data Scraping & Cleaning** - Custom web scraping pipeline for real estate data
- **Exploratory Data Analysis (EDA)** - Comprehensive data visualization and insights
- **Multiple Regression Models:**
  - Linear Regression
  - Decision Tree Regression
  - Random Forest Regression
  - Support Vector Regression
- **Model Training & Evaluation** - Cross-validation and performance metrics
- **Pipeline Creation & Saving** - Automated ML pipeline for production use
- **Deployment** - Streamlit web app hosted on AWS

## 📁 Dataset

The dataset was **self-scraped** from real estate websites and preprocessed specifically for this project. It includes features such as:

- Location/Area
- Number of BHK (Bedrooms, Hall, Kitchen)
- Total square footage
- Property age
- Amenities
- Price per square foot

## 🛠️ Tech Stack

- **Python 3.11.9**
- **Machine Learning:** scikit-learn
- **Data Processing:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Web App:** Streamlit
- **Deployment:** AWS
- **Development:** Jupyter Notebook

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/house-price-prediction.git
cd house-price-prediction
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Linux/Mac:
source venv/bin/activate

# For Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Project
```bash
# Launch Jupyter Notebook
jupyter notebook House_Price_Prediction.ipynb

# Or run the Streamlit app directly
streamlit run app.py
```

## 📦 Requirements

Create a `requirements.txt` file with:
```
pandas>=1.5.0
numpy>=1.24.0
scikit-learn>=1.3.0
seaborn>=0.12.0
matplotlib>=3.6.0
jupyter>=1.0.0
streamlit>=1.28.0
plotly>=5.15.0
```

## ⚠️ Important Notes

> **Model File Notice:**  
> The trained model `pipeline.pkl` is **not included** in this repository due to GitHub's file size limitations (>100MB). 
> 
> **Solution:** Run the notebook end-to-end to retrain and generate the model file locally.

## 🚀 Deployment

This project features a **live web application** built with Streamlit and deployed on AWS:

- **Frontend:** Interactive Streamlit dashboard
- **Backend:** Trained ML pipeline
- **Hosting:** AWS EC2/Elastic Beanstalk
- **Live Demo:** [Coming Soon] 🔗

## 📈 Model Performance

| Model | R² Score | RMSE | MAE |
|-------|----------|------|-----|
| Linear Regression | 0.85 | 2.34M | 1.89M |
| Decision Tree | 0.82 | 2.67M | 2.01M |
| Random Forest | 0.89 | 2.12M | 1.76M |

*Note: Actual performance metrics will be updated after model training*

## 🔍 Project Structure

```
house-price-prediction/
│
├── data/
│   ├── raw/                 # Original scraped data
│   └── processed/           # Cleaned and feature-engineered data
│
├── notebooks/
│   └── House_Price_Prediction.ipynb
│
├── src/
│   ├── data_scraping.py     # Web scraping scripts
│   ├── preprocessing.py     # Data cleaning functions
│   └── model_training.py    # ML model implementations
│
├── models/
│   └── pipeline.pkl         # Trained model (generated locally)
│
├── app.py                   # Streamlit web application
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## 🎯 Key Learnings

- **Web Scraping:** BeautifulSoup and Selenium for data extraction
- **Feature Engineering:** Creating meaningful predictors from raw data
- **Model Selection:** Comparing multiple algorithms for optimal performance
- **MLOps:** Building reproducible ML pipelines
- **Deployment:** End-to-end application deployment on cloud platforms

## 👤 Author

**Priyanshu Singh**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](#)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](#)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](#)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgements

- Thanks to the open-source community for the amazing libraries
- Inspiration from various ML practitioners and their public projects
- Special thanks to online resources and tutorials that guided this learning journey

---

⭐ **If you found this project helpful, please give it a star!** ⭐

