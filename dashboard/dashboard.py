import streamlit as st
import nbformat
from nbconvert import PythonExporter
import matplotlib.pyplot as plt
import pandas as pd

# Path to the uploaded Jupyter notebook
NOTEBOOK_PATH = './analysis_data.ipynb'

# Load the Jupyter notebook
def load_notebook(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)

# Convert Jupyter notebook to Python code
def convert_notebook_to_python(nb):
    exporter = PythonExporter()
    python_code, _ = exporter.from_notebook_node(nb)
    return python_code

# Execute the converted notebook code and capture matplotlib figures
def run_notebook_code(python_code, globals_dict):
    exec(python_code, globals_dict)

# Streamlit App Interface
def main():
    st.title("Ecommerce Analysis Dashboard")

    # Define your business question here
    st.subheader("Business Question: What are the sales trends for the top categories?")

    # Load and convert notebook
    notebook_content = load_notebook(NOTEBOOK_PATH)
    python_code = convert_notebook_to_python(notebook_content)

    # Automatically run the notebook
    output_globals = {}

    # Clear any previous figures in case notebook contains multiple plot commands
    plt.close('all')
    
    # Run the notebook code and capture output
    run_notebook_code(python_code, output_globals)
    
    # Display specific variables that answer the business question
    st.subheader("Sales Trend Analysis:")
    
    # Display DataFrame (if any)
    if "sales_trend_df" in output_globals:  # Replace with your variable names from the notebook
        st.dataframe(output_globals["sales_trend_df"])  # Display the DataFrame with sales trends
        st.markdown("""
        **Penjelasan:**
        Tabel di atas menunjukkan tren penjualan berdasarkan kategori produk. Anda dapat melihat setiap baris yang mewakili jumlah penjualan untuk kategori produk tertentu selama periode waktu yang dianalisis. 
        Informasi ini penting untuk mengidentifikasi kategori yang menunjukkan pertumbuhan atau penurunan dalam penjualan.
        """)
    
    # Display any matplotlib figures related to the question
    st.subheader("Generated Plots:")
    figures = [plt.figure(i) for i in plt.get_fignums()]
    
    if not figures:
        st.write("No plots were generated.")
    else:
        # Render and display each plot in Streamlit
        for fig in figures:
            st.pyplot(fig)
            st.markdown("""
            **Penjelasan Grafik:**
            Grafik ini menunjukkan tren penjualan dari waktu ke waktu untuk berbagai kategori produk. 
            Naiknya garis menunjukkan peningkatan penjualan, sementara garis yang menurun menunjukkan penurunan dalam penjualan.
            Grafik ini dapat membantu dalam pengambilan keputusan untuk mengalokasikan sumber daya ke produk-produk dengan performa terbaik.
            """)

if __name__ == "__main__":
    main()
