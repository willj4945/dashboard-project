import streamlit as st
import pandas as pd
import numpy as np

# CSV file path
csv_file_path = "data/quarterly_canada_population.csv"

# Function to load data from CSV file
@st.cache_data()
def load_data(file_path):
    return pd.read_csv(file_path, dtype={
        'Quarter': str,
        'Canada': np.int32,
        'Newfoundland and Labrador': np.int32,
        'Prince Edward Island': np.int32,
        'Nova Scotia': np.int32,
        'New Brunswick': np.int32,
        'Quebec': np.int32,
        'Ontario': np.int32,
        'Manitoba': np.int32,
        'Saskatchewan': np.int32,
        'Alberta': np.int32,
        'British Columbia': np.int32,
        'Yukon': np.int32,
        'Northwest Territories': np.int32,
        'Nunavut': np.int32
    })

# Function to save the DataFrame back to the CSV file
def save_data(df, file_path):
    df.to_csv(file_path, index=False)

# Load the DataFrame into session state if not already loaded
if 'df_canada' not in st.session_state:
    st.session_state.df_canada = load_data(csv_file_path)

# Streamlit page title
st.title("Population of Canada")

# Form for editing the DataFrame
with st.form(key="User update Form"):
    st.write("### Edit DataFrame")
    row_to_update = st.number_input("Select Row Index to Edit", min_value=0, max_value=len(st.session_state.df_canada) - 1, step=1)
    column_to_update = st.selectbox("Select Column to Edit", st.session_state.df_canada.columns)
    new_value = st.text_input(f"New Value for {column_to_update}")

    # Update the DataFrame when the button is clicked
    if st.form_submit_button("Update"):
        try:
            # Convert the new value to the appropriate type before assigning
            new_value = int(new_value) if column_to_update != 'Quarter' else new_value

            # Update the DataFrame in session state
            st.session_state.df_canada.at[row_to_update, column_to_update] = new_value

            # Save the updated DataFrame to the CSV file
            save_data(st.session_state.df_canada, csv_file_path)

            st.success("DataFrame Updated and Saved to CSV!")
        except ValueError:
            st.error(f"Invalid value for column '{column_to_update}'. Please enter the correct data type.")