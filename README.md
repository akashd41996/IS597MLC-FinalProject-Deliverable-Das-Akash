# IS597MLC: E-Commerce Customer Satisfaction Analysis

## Dataset Overview

This repository contains analysis of the Brazilian E-Commerce Public Dataset by Olist, provided through Kaggle. It spans over 100,000 orders from 2016 to 2018 across multiple Brazilian marketplaces and includes details on order status, pricing, payment, delivery performance, customer location, product attributes, and reviews.

### Data Source
- **Provider**: Olist Store, Andre Sionek, Dabague Francisco, Magioli
- **Data Link**: [Kaggle Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data)

### Dataset Description
- **Data Size**: Information on 100,000 orders from 2016 to 2018.
- **Attributes**: The dataset includes extensive details across customer and order metrics.
  - `customer_id`: Key to orders dataset, unique per order.
  - `customer_unique_id`: Unique identifier for a customer.
  - `order_status`: Status of the order (e.g., delivered, shipped).
  - `order_purchase_timestamp`: Timestamp when the purchase was made.
  - `review_score`: Customer satisfaction score, from 1 to 5.
  - Additional attributes include geolocation data, payment details, and more.

## Repository Structure

- `/data`: Directory containing the zipped dataset files. Ensure that you unzip these files in this directory.
- `IS597MLC_Exploratory_Data_Analysis_Final_Project_Das_Akash.ipynb`: Jupyter notebook for exploratory data analysis.
- `IS597-MLC-Machine_Learning_Pipeline_Final_Project_Das_Akash.ipynb`: Jupyter notebook for machine learning pipeline.
- `import_data_final.py`: Python script for loading and preprocessing the data.

## Getting Started

To replicate this analysis, follow the steps below:

### Prerequisites
Ensure that Python 3.x is installed on your system. You will need Jupyter Notebook or JupyterLab to run the notebooks. Install the necessary Python packages using:

```bash
pip install notebook pandas matplotlib seaborn scikit-learn geopandas xgboost imblearn
