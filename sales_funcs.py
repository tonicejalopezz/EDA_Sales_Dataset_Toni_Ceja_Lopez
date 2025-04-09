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

    data["profit"] = ((data["Unit_Price"] * (1 - data["Discount"])) - data["Unit_Cost"]) * data["Quantity_Sold"]

    # Drop Sale_Date column
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

def bivariate_analysis(data, column_1, column_2):
    """
    Function to display bivariate analysis.
    """
    categorical_columns = data.select_dtypes(include=["object"]).columns

    for col in categorical_columns:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=data, x=column_1, y=column_2, hue=col, palette="Set2")

        plt.title(f"Bivariate Analysis of {column_1} and {column_2}")
        plt.xlabel(column_1)
        plt.ylabel(column_2)
        plt.grid(alpha=0.5)
        plt.show()

def violin_plot_analysis(data):
    """
    Function to display violin plot analysis of categorical & numerical variablues
    """
    # Selected columns for box plot analysis

    wanted_cat_cols = data[["Sales_Rep", "Region", "Product_Category", "Customer_Type", "Payment_Method", "Sales_Channel"]].columns
    wanted_num_cols = data[["Sales_Amount","Quantity_Sold", "profit"]].columns

    for cat_col in wanted_cat_cols:

        fig, axs = plt.subplots(3, figsize=(12, 15))
        fig.suptitle(f"Box Plot of {cat_col}")

        for idx, num_col in enumerate(wanted_num_cols):

            sns.violinplot(data=data, x=cat_col, y=num_col, ax=axs[idx], hue=cat_col, 
                           inner_kws=dict(box_width=20, whis_width=5), palette="Set2_r")

            axs[idx].set_xlabel(" ")
            axs[idx].grid(alpha=0.5)

        plt.show()

def grouping_column(data, selected_column=None, by_column=None):
        """
        Grouping by selected column and returning sum, mean, and count of desired columns.
        """

        select_sums = (data.groupby(selected_column)
                       [[by_column]].sum().add_prefix("Total_"))
        
        select_means = (data.groupby(selected_column)
                        [[by_column]].mean().add_prefix("Average_"))
        
        select_counts = (data.groupby(selected_column)
                         [[by_column]].count().add_prefix("Count_"))
    
        group_data =  pd.concat([select_sums, select_means, select_counts], axis=1).reset_index()

        return group_data

def rep_piv_table(data, selected_column=None, by_column=None):
    """
    Creating a pivot table for sales rep.
    """

    rep_pivot = data.pivot_table(index=selected_column, 
                                values=by_column, 
                                aggfunc=["sum"])
    
    table = rep_pivot.stack(future_stack=True).reset_index().rename(columns={"level_1": "Type"})
    
    return table

def plot_visual(data, column_1, columns):
    """
    Displaying Line Plot
    """
    fig, axs = plt.subplots(len(columns), 1, figsize=(12, 6 * len(columns)))
    colors = sns.color_palette("tab10")
    fig.suptitle(f"Line Plot by {column_1}")

    for i, col in enumerate(columns):

        axs[i].plot(data[column_1], data[col], marker='o', label=col, color=colors[i])
        axs[i].set_ylabel(col)
        axs[i].grid(alpha=0.5)
        axs[i].legend()
        axs[i].grid(alpha=0.5)

    axs[i].set_xlabel(column_1)

    plt.tight_layout(pad=2)
    plt.show()