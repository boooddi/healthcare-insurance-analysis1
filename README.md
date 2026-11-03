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

### Dataset Source and Licence 
The dataset was obtained from Kaggle: [Healthcare Insurance Dataset](https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance) 

The Kaggle dataset page identifies the licence as **CC0: Public Domain**. This permits reuse of the dataset under the terms of that licence. The original source has been retained in the project, separately from the cleaned dataset. 

The dataset description credits Willian Oliveira and lists Arun Jangir and Willian Oliveira. It states that the data was collected through conversations with people in hospitals and from insurance-related information available online. The collection process and representativeness of the data could not be independently verified.

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

## Data Lineage and Processing 
The project follows a clear data processing workflow: 

1. **Data source:** The original healthcare insurance dataset was downloaded from Kaggle and saved as `data/insurance.csv`. 

2. **Data inspection:** Python and pandas were used to inspect the dataset, including its structure, data types, missing values, duplicate records, and category values. 

3. **Data cleaning:** One exact duplicate record was removed. The original dataset was preserved, and no missing values were found. 

4. **Cleaned dataset:** The resulting dataset contains 1,337 records and 7 columns and was saved as `data/insurance_cleaned.csv`. 

5. **Analysis:** The Jupyter Notebook uses the cleaned dataset to calculate statistics, investigate patterns, and produce visualisations. 

6. **Dashboard:** The Streamlit application uses the cleaned dataset to present interactive charts and findings. 

Keeping the original and cleaned datasets separate helps preserve the source data and makes the cleaning process easier to review.

## Key Findings 

- **Smoking status:** Smokers had a mean recorded charge of approximately 32,050.23, compared with 8,440.66 for non-smokers. 
- **Age:** The correlation between age and recorded charges was approximately 0.298, indicating a weak positive linear relationship. 
- **BMI:** The correlation between BMI and recorded charges was approximately 0.198, also indicating a weak positive linear relationship. 
- **Region:** The southeast had the highest mean recorded charges, approximately 14,735.41. The southwest had the lowest mean, approximately 12,346.94. 
- **Distribution:** Recorded charges were right-skewed, with the mean higher than the median. These findings describe associations within this dataset. They do not establish that smoking, age, BMI or region causes differences in charges. 

## Project Structure

```text
healthcare-insurance-analysis1/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── insurance.csv
│   └── insurance_cleaned.csv
└── notebooks/
    └── healthcare_insurance_analysis1.ipynb
```

- `data/`: Contains the original and cleaned datasets.
- `notebooks/`: Contains the Jupyter Notebook with data preparation, analysis and visualisations.
- `app.py`: Contains the Streamlit dashboard application.
- `requirements.txt`: Lists the Python packages required to run the project.
- `README.md`: Provides project information and setup instructions.

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

### Running the Jupyter Notebook 
To open and run the analysis notebook: 
1. Activate the project virtual environment. 
2. Install Jupyter if it is not already installed: ```bash pip install jupyter ``` 
3. Start Jupyter: ```bash jupyter notebook ``` 
4. Open `notebooks/healthcare_insurance_analysis1.ipynb`. 
5. Run the notebook cells in order to reproduce the analysis and visualisations. 

Make sure the project dependencies have been installed using `pip install -r requirements.txt` before running the notebook.

## Limitations and Ethical Considerations 

The dataset's collection method and representativeness are not fully verifiable from the available source description. The currency and units of recorded charges are also unspecified. The analysis is descriptive and does not prove causation. 
Other variables may contribute to observed differences. Findings should not be treated as personalised medical advice or definitive evidence for insurance pricing decisions. Before redistributing the dataset through a public repository, its licence and sharing permissions should be checked. 

## Links 
- **GitHub repository:** [GitHub repository](https://github.com/boooddi/healthcare-insurance-analysis1)
- **Live Streamlit dashboard:** [Live Streamlit dashboard](https://healthcare-insurance-analysis1-juxdgjmwrqd46sfcjmbc9i.streamlit.app/) 


## References 
- Oliveira, W. (n.d.). *Healthcare Insurance Dataset*. Kaggle. https://www.kaggle.com/datasets/willianoliveiragibin/healthcare-insurance 
- pandas documentation. https://pandas.pydata.org/docs/ 
- NumPy documentation. https://numpy.org/doc/ 
- Matplotlib documentation. https://matplotlib.org/stable/ 
- Seaborn documentation. https://seaborn.pydata.org/ 
- Streamlit documentation. https://docs.streamlit.io/

## AI Use and Acknowledgement 

ChatGPT was used as a support tool during this project to help with Python coding, troubleshooting errors, understanding data analysis techniques, developing the Streamlit dashboard, and improving project documentation. 

AI-generated suggestions were reviewed and adapted where appropriate. Code was tested by running it, checking the outputs, and validating the cleaned dataset and dashboard results. The final analysis, decisions, and interpretation were reviewed by the learner. 

AI assistance was used to support learning and development; it did not replace checking the accuracy of the results or understanding the work.

## Conclusion 
This project demonstrates how Python can be used to clean, analyse and visualise healthcare insurance data. The results identify patterns in recorded charges and show how data analysis can support evidence-based investigation while recognising the limitations of the dataset.

