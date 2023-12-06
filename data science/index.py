# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the housing dataset (replace 'housing_dataset.csv' with your actual dataset file)
housing_df = pd.read_csv('housing_dataset.csv')

# Display basic information about the housing dataset
print(housing_df.info())

# Display summary statistics of housing prices
print(housing_df['SalePrice'].describe())

# Check for missing values in the dataset
print(housing_df.isnull().sum())

# Visualize the distribution of housing prices
sns.histplot(housing_df['SalePrice'], bins=20, kde=True)
plt.title('Distribution of Housing Prices')
plt.show()

# Visualize the relationship between living area and housing prices
sns.scatterplot(x='GrLivArea', y='SalePrice', data=housing_df)
plt.title('Scatter Plot of Living Area vs Housing Prices')
plt.show()

# Visualize the correlation matrix of numerical variables
correlation_matrix = housing_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Variables')
plt.show()

# Perform a statistical test (e.g., correlation test between two variables)
from scipy.stats import pearsonr

corr_coefficient, p_value = pearsonr(housing_df['GrLivArea'], housing_df['SalePrice'])
print(f'Correlation Coefficient: {corr_coefficient}, P-Value: {p_value}')

# Further analysis and visualization based on your project goals

# Save the visualizations or results if needed
# plt.savefig('housing_analysis_visualizations.png')

# Close any open plots
plt.close('all')
