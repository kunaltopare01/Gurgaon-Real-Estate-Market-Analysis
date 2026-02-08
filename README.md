
# Gurgaon Real Estate Market Analysis 🏙️

## 📌 Project Overview
This project focuses on **Exploratory Data Analysis (EDA)** of residential real estate properties in **Gurgaon**.  
The goal is to analyze pricing patterns and derive **data-backed insights** that can help buyers, investors, and developers make informed decisions.

The analysis is performed using Python and covers pricing trends, locality-wise comparisons, property features, and the impact of regulatory approval (RERA).

---

## 🎯 Objectives
- Understand price distribution across different localities
- Analyze the effect of area (sqft), BHK configuration, and property type on price
- Compare ready-to-move and under-construction properties
- Evaluate whether RERA-approved properties command a price premium
- Identify builders who consistently price higher
- Study price behavior on a per square foot basis

---

## 📊 Business Questions Answered
1. Which is the costliest flat in the dataset?
2. Which locality has the highest average price?
3. Which locality has the highest rate per square foot?
4. Do ready-to-move properties cost more than under-construction properties?
5. Do RERA-approved properties command a price premium?
6. How does area (sqft) impact property price?
7. Which BHK configuration is most expensive on a per sqft basis?
8. Which property type (Apartment, Floor, Plot) is the costliest?
9. Do certain builders consistently price higher?
10. Are larger homes always more expensive per square foot?

---

## 🛠️ Tools & Technologies
- **Python**
- **Pandas** – data cleaning and manipulation
- **Matplotlib** – data visualization
- **Seaborn** – statistical and exploratory plots
- **Jupyter Notebook** – EDA and analysis workflow

---

## 📁 Project Structure

```text
gurgaon-real-estate-analysis/
│
├── main.py              # Executable Python script
├── analysis.ipynb       # EDA notebook with visualizations
├── data.csv             # Dataset used for analysis
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── .gitignore
└── images/
    ├── area_vs_price.png
    └── area_vs_rate_per_sqft.png
```
---

## 🚀 How to Run the Project

1. Clone the repository
   
git clone https://github.com/kunaltopare01/gurgaon-real-estate-market-analysis.git


2. Navigate to the project folder

  
   cd gurgaon-real-estate-analysis
  
3. Install required libraries

  
   pip install -r requirements.txt
   
4. Run the analysis script

  
   python main.py
   

---

## 📈 Key Insights

* Premium localities in Gurgaon command significantly higher prices and rate per square foot
* Under-construction properties are priced higher than ready-to-move properties in this dataset
* RERA-approved properties do not show a significant price premium
* Builder reputation has a noticeable impact on property pricing
* Larger homes are not always more expensive on a per square foot basis
* Certain extreme values (e.g., unusually high BHK counts) indicate data anomalies requiring further cleaning

---

## 📚 Dataset Information

* Dataset: Gurgaon Residential Real Estate Listings
* Source: Kaggle
* Usage: Educational and learning purposes only

---

## 👤 Author

**Kunal Topare**
Aspiring Data Analyst
Skills: Python | EDA | Pandas | Data Visualization

---

