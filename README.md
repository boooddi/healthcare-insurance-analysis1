# Healthcare Insurance Cost Analysis 
## Project Overview 
This project analyses a healthcare insurance dataset using Python and data analytics techniques. The aim is to explore how recorded healthcare insurance charges vary according to smoking status, age, BMI and geographical region. The project uses data cleaning, descriptive statistics, data grouping and visualisations to identify patterns that may support better understanding of healthcare insurance costs. 
## Business Questions 
The analysis investigates the following questions: 
1. How do recorded charges differ between smokers and non-smokers? 
2. What relationship can be observed between age and recorded charges? 
3. How do mean and median recorded charges compare across regions? 
4. What relationship can be observed between BMI and recorded charges? 
## Dataset 
The dataset was obtained from Kaggle: [Healthcare Insurance Dataset](https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance) It contains 1,338 original records and seven columns: `age`, `sex`, `bmi`, `children`, `smoker`, `region` and `charges`. One exact duplicate row was removed, leaving 1,337 records in the cleaned dataset. No missing values were identified. The dataset description does not specify the currency or precise units for `charges`. Results are therefore described as recorded charges rather than assuming a particular currency. 
## Tools and Technologies 
- Python 
- pandas 
- NumPy 
- Matplotlib 
- Seaborn 
- Jupyter Notebook 
- Streamlit 
## Data Preparation 
The dataset was loaded into pandas for inspection and cleaning. The preparation process included: 
- Checking data types, missing values and duplicate records. 
- Checking category values and negative numerical values. 
- Removing one exact duplicate while preserving the original dataset. 
- Saving and validating the cleaned dataset as a separate CSV file. 
## Key Findings 
- **Smoking status:** Smokers had a mean recorded charge of approximately 32,050.23, compared with 8,440.66 for non-smokers. 
- **Age:** The correlation between age and recorded charges was approximately 0.298, indicating a weak positive linear relationship. 
- **BMI:** The correlation between BMI and recorded charges was approximately 0.198, also indicating a weak positive linear relationship. 
- **Region:** The southeast had the highest mean recorded charges, approximately 14,735.41. The southwest had the lowest mean, approximately 12,346.94. 
- **Distribution:** Recorded charges were right-skewed, with the mean higher than the median. These findings describe associations within this dataset. They do not establish that smoking, age, BMI or region causes differences in charges. 
## Project Structure 
```
text healthcare-insurance-analysis1/ 
├── app.py 
├── requirements.txt 
├── README.md 
├── .gitignore 
├── data/ │ 
├── insurance.csv 
│ └── insurance_cleaned.csv 
└── notebooks/ └
── healthcare_insurance_analysis1.ipynb 
``` 
## How to Run the Project 
### 1. Clone or download the project 
Download the repository from GitHub or clone it using Git. 
### 2. Create and activate a virtual environment 
On macOS or Linux: ```bash python3 -m venv .venv source .venv/bin/activate ``` 
### 3. Install the required packages 
```bash python -m pip install -r requirements.txt ``` 
### 4. Run the Streamlit dashboard 
From the main project folder, run: 
```bash streamlit run app.py ``` 
The dashboard should open in your web browser. 
### 5. Explore the notebook 
Open `notebooks/healthcare_insurance_analysis1.ipynb` in VS Code or Jupyter Notebook to review the data preparation, statistical analysis, charts and interpretations. 
## Limitations and Ethical Considerations 
The dataset's collection method and representativeness are not fully verifiable from the available source description. The currency and units of recorded charges are also unspecified. The analysis is descriptive and does not prove causation. Other variables may contribute to observed differences. Findings should not be treated as personalised medical advice or definitive evidence for insurance pricing decisions. Before redistributing the dataset through a public repository, its licence and sharing permissions should be checked. 
## Links 
- **GitHub repository:** [follow link](https://github.com/boooddi/healthcare-insurance-analysis1)
- **Live Streamlit dashboard:** [follow link](https://healthcare-insurance-analysis1-juxdgjmwrqd46sfcjmbc9i.streamlit.app/) 
## Conclusion 
This project demonstrates how Python can be used to clean, analyse and visualise healthcare insurance data. The results identify patterns in recorded charges and show how data analysis can support evidence-based investigation while recognising the limitations of the dataset.