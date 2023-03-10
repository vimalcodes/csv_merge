import streamlit as st
import pandas as pd


@st.cache

def convert_df(raw_data):

# IMPORTANT: Cache the conversion to prevent computation on every rerun

    return raw_data.to_csv(index=False).encode('utf-8')

st.title("File Merger App")
st.write("Merge Multiple CSV files using Python")

st.header("Import your File")
st.write("Data from first file uploaded will be first, followed by the next file chosen")
st.write("Drop all at once or one by one (If it follows sequence)")

uploaded_files = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=True)
if st.button('Merge'):
    for file in uploaded_files:
        file.seek(0)
    uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    raw_data = pd.concat(uploaded_data_read)

    csv = convert_df(raw_data)

    st.download_button(label="Download data as CSV", data=csv, file_name='mergefile.csv', mime='text/csv')

