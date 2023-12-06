from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = Flask(__name__)

# Load your dataset (replace 'housing_dataset.csv' with your actual dataset file)
housing_df = pd.read_csv('housing_dataset.csv')

# ... Your Python code for data analysis and visualization ...

# Function to generate base64-encoded image for HTML display
def plot_to_base64(plot):
    img = BytesIO()
    plot.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

# Routes
@app.route('/')
def home():
    # Generate your visualizations
    plt.figure(figsize=(8, 6))
    sns.histplot(housing_df['SalePrice'], bins=20, kde=True)
    plt.title('Distribution of Housing Prices')
    plot_data = plot_to_base64(plt)
    return render_template('index.html', plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)
