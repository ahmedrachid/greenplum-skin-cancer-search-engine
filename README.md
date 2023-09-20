# Skin Cancer Images - Semantic Search

This repository provides instructions and code for setting up a Skin Cancer Image Semantic Search engine leveraging VMware Greenplum as Vector Database.

![Streamlit App](streamlit_app.gif)

## Getting Started

Follow these steps to set up the Skin Image Search System on your local machine.

### Prerequisites

- [Greenplum Database](https://greenplum.org/)
- [pgvector extension](https://github.com/pgvector/pgvector)
- Jupyter Notebook
- Python dependencies (requirements.txt)

### Step 1: Create Database Tables and Python Setup

1. Run the `script.sql` file to create tables for storing images, metadata and embeddings in your Greenplum database:

    ```bash
    $ psql -U your_username -d your_database -a -f script.sql
    ```
2. Install the required Python packages listed in `requirements.txt`.
   ```bash
    $ pip install -r requirements.txt
   ```
### Step 2: Generate Embeddings
1. Use the `Skin_Cancer_Image_Semantic_Search.ipynb` Notebook to download the dataset and generate embeddings into Greenplum.

### Step 3: Run and Access the Web App
1. Run the Streamlit App using:
   ```bash
    $ streamlit run app.py
   ```
2. Access the web application by opening a web browser and navigating to:

    ```
    http://localhost:8501
    ```
