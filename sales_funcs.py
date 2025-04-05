# Functions to clean the data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data cleaning function for Exploratory Data Analysis
def clean_data(data):
    """
    Data cleaning function for Exploratroy Data Analysis.
    """
    # Conditional statements for data cleaning.

    # Split Sale Data to extract year, month, day, and day of week
    data["Sale_Date"] = pd.to_datetime(data["Sale_Date"])
    data["Year"] = data["Sale_Date"].dt.year
    data["Month"] = data["Sale_Date"].dt.month
    data["Day"] = data["Sale_Date"].dt.day
    data["Day_of_Week"] = data["Sale_Date"].dt.day_name()

    data["profit"] = data["Sales_Amount"] - data["Unit_Cost"] * data["Quantity_Sold"]

    # Drop Sale_data column
    data = data.drop(columns=["Sale_Date"])

    # Check for missing values
    if data.isnull().values.any():

        # fill categorical missing values with most frequent value
        for column in data.select_dtypes(include=["object"]).columns:
            data[column] = data[column].fillna(data[column].mode().iloc[0])

        # Fill numerical missing values with mean
        for column in data.select_dtypes(include=["number"]).columns:
            data[column] = data[column].fillna(data[column].mean())

    # Check for duplicates
    if data.duplicated().sum() > 0:

        # Drop duplicates rows
        data = data.drop_duplicates()
    
    return data

def univariate_analysis(data):
    """
    Function to display univariate analysis.
    """

    # Customizable color palette
    palette = sns.color_palette("tab20")

    for i, column in enumerate(data.columns):

        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], color=palette[i], shrink=0.8)

        # This only applies to categorical variables with more than 10 unique values
        
        if data[column].dtype == "object" and data[column].nunique() > 10:
            plt.xticks(rotation=45)
    
        plt.title(f"Univariate Analysis of {column}")
        plt.xlabel(column)
        plt.grid(alpha=0.5)
        plt.show()

def corr_matrix(data):
    """
    Function to display correlation matrix.
    """

    numerical_columns = data.select_dtypes(include=["number"]).columns

    plt.figure(figsize=(12, 8))
    sns.heatmap(data[numerical_columns].corr(), annot=True, cmap="coolwarm_r", fmt=".2f")

    plt.title("Numerical Columns Correlation Matrix")
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.show()