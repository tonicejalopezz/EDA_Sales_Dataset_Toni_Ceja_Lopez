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

    palette = sns.color_palette("tab20")

    for i, column in enumerate(data.columns):

        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], color=palette[i], kde=True)

        plt.title(f"Univariate Analysis of {column}")
        plt.xlabel(column)
        plt.grid(alpha=0.5)
        plt.show()