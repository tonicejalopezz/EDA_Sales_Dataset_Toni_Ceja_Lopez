# Exploratory Data Analysis Sales Dataset

Conducted using Python with libraries such as Pandas, NumPy, Matplotlib, and Seaborn. 

## Data Source

The following Dataset was used from Kaggle. 
Link: https://www.kaggle.com/datasets/vinothkannaece/sales-dataset/data

## Files

*   [sales_proj.ipynb](sales_proj.ipynb): A Jupyter Notebook containing the main analysis workflow.
*   [sales_funcs.py](sales_funcs.py): A Python script containing custom functions used in the analysis.

## Analysis Workflow in `sales_proj.ipynb`

1.  **Importing Data from Kaggle:**
    *   The notebook starts by importing necessary libraries and downloading the sales dataset from Kaggle using the `kagglehub` library.
2.  **Data Loading and Inspection:**
    *   The dataset is loaded into a Pandas DataFrame, and the first few rows are displayed using `data.head()`.
    *   Descriptive statistics are generated using `data.describe()` to understand the distribution of numerical features.
    *   Data types of each column are inspected using `data.dtypes`.
3.  **Data Cleaning:**
    *   The `clean_data` function from [sales_funcs.py](sales_funcs.py) is used to clean the data. This involves:
        *   Extracting year, month, day, and day of the week from the `Sale_Date` column.
        *   Calculating the profit for each transaction.
        *   Handling missing values by filling categorical columns with the most frequent value.
4.  **Univariate Analysis:**
    *   The `univariate_analysis` function from [sales_funcs.py](sales_funcs.py) is used to visualize the distribution of individual columns using histograms.
5.  **Correlation Matrix & Bivariate Analysis:**
    *   The `corr_matrix` function from [sales_funcs.py](sales_funcs.py) displays the correlation matrix to identify relationships between numerical features.
    *   The `bivariate_analysis` function from [sales_funcs.py](sales_funcs.py) is used to analyze the relationship between `Discount` and `profit`, and `Quantity_Sold` and `profit`.
6.  **Violin Plot Analysis:**
    *   The `violin_plot_analysis` function from [sales_funcs.py](sales_funcs.py) is used to display violin plots for relevant numerical values for each relevant categorical value.
7.  **Sales Analysis by Time:**
    *   Sales data is grouped by month and day of the week to identify trends.
    *   The `grouping_column` function from [sales_funcs.py](sales_funcs.py) is used to group data and calculate total, average, and count of sales amount and quantity sold.
    *   The `plot_visual` function from [sales_funcs.py](sales_funcs.py) is used to visualize the sales trends.
8.  **Sales Representative Region Reports:**
    *   The `rep_piv_table` function from [sales_funcs.py](sales_funcs.py) is used to create a pivot table for sales representatives, showing the quantity sold and sales amount.
    *   The data is then sorted to identify the sales representatives with the highest quantity sold and total sales amount.

## Functions in `sales_funcs.py`

*   [`clean_data(data)`](sales_funcs.py)
*   [`univariate_analysis(data)`](sales_funcs.py)
*   [`corr_matrix(data)`](sales_funcs.py)
*   [`bivariate_analysis(data, column_1, column_2)`](sales_funcs.py)
*   [`violin_plot_analysis(data)`](sales_funcs.py)
*   [`grouping_column(data, selected_column=None, by_column=None)`](sales_funcs.py)
*   [`rep_piv_table(data, selected_column=None, by_column=None)`](sales_funcs.py)
*   [`plot_visual(data, column_1, columns)`](sales_funcs.py)