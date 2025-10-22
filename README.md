## 📊 Learner Performance Analysis: Student Scores

This repository contains the analysis of student performance data to identify patterns and inform future educational interventions. The analysis was conducted using **Python** (specifically **pandas** within a **Jupyter Notebook**) and is summarized in an executive-ready format in an accompanying **Excel** file (not included in this repository, but mentioned in the original scope).

### 🎯 Objective

The primary goal of this project was to explore learner performance patterns using the provided dataset, *Week-5-Student-Scores.csv*, focusing on data quality, descriptive statistics, and identifying key distributions in performance metrics.

***

### 🛠️ Tools and Libraries

* **Python 3.x**
* **pandas** (for data manipulation and analysis)
* **matplotlib** and **seaborn** (for data visualization, implicitly used for histograms/boxplots)
* **Jupyter Notebook** (for interactive development and documentation)

***

### 📁 Repository Contents

* `Learner_Performance_Analysis.ipynb`: The main **Jupyter Notebook** containing all the Python code for data loading, quality checks, descriptive statistics, and visualization.
* `Week-5-Student-Scores.csv`: The dataset used for the analysis.

***

### 📝 Overview of Analysis

The analysis followed the two main questions outlined in the project brief.

#### Q1 — Data Readiness & Quality Checks

This phase focused on ensuring the data was clean and ready for analysis.

* **Data Loading & Reporting:** The CSV file was loaded, and initial checks were performed to report on the dataset's shape, column data types, and counts of missing values and duplicates.
* **Data Quality Decisions:** A table was generated summarizing the diagnostics. Decisions regarding missing data imputation, dropping records, or retaining them were briefly justified. Similarly, a decision on handling duplicate records was outlined.
    * *Self-Correction/Imputation/Dropping:* (Specific method would be detailed in the bullet points in the notebook.)

#### Q2 — Descriptive Statistics & Distributions

This phase explored the central tendencies and spread of the key numeric variables.

* **Descriptive Statistics Table:** A compact table was produced containing the **mean**, **median**, **standard deviation (std)**, **minimum**, **maximum**, and the **25th, 50th, and 75th percentiles** for all relevant numeric fields.
* **Visualization:** **Histograms** or **boxplots** were generated to visualize the distributions of the following key metrics:
    * `Final_Score`
    * `Study_Hours_per_Week`
    * `Attendance_Rate`
* **Distribution Commentary:** A concise explanation was provided in the notebook discussing observations related to **skewness** and the presence of **outliers** in the visualized distributions, and what these findings might imply regarding the learner population's performance and habits.
