import streamlit as st
import pandas as pd

from logics import NumericColumn

def display_tab_num_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_num_content (function): Function that will instantiate tab_num.logics.NumericColumn class, save it into Streamlit session state and call its tab_num.logics.NumericColumn.find_num_cols() method in order to find all numeric columns.
    Then it will display a Streamlit select box with the list of numeric columns found.
    Once the user select a numeric column from the select box, it will call the tab_num.logics.NumericColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_num.logics.NumericColumn.get_summary() as a Streamlit Table
    - the graph from tab_num.logics.NumericColumn.histogram using Streamlit.altair_chart()
    - the results of tab_num.logics.NumericColumn.frequent using Streamlit.write
 
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded dataframe (optional)

    --------------------
    Returns
    --------------------
    -> None

    """
    instance = NumericColumn()
    data_columns = ['random string', 'random string1', 'random string 2']

    select_column = st.selectbox("Which numeric column do you want to explore", data_columns)

    # Based on select_column, generate below data
    # instance.set_data(select_column)
    # num = instance.get_summary(<Get Numeric Column Table>)
    num = {
        'Description': [
            "Number of Unique Values",
            "Number of Missing Values",
            "Number of Ocurrence of 0 Value",
            "Number of Negative Values",
            "The Average Value",
            "The Standard Deviation Value",
            "The Minimum Value",
            "The Maximum Value",
            "The Median Value"
            ],
        'Value': [0, 0, 0, 0, 0, 0, 0, 0, 0]
    }


    num_column = pd.DataFrame(num)

    st.write("Numeric Column")
    st.table(num_column)
    
    # instance.set_histogram()
    # st.altair_chart(instance.histogram)

    #num = instance.get_summary(<Get Most Frequent Values Table>) 
    freq = {
        'value': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'occ': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'percentage': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    freq_Data = pd.DataFrame(freq)

    st.write("Most Frequent Values")
    st.table(freq_Data)
    
def dataframe():
    st.write("This is the dataframe.")

def text_series():
    st.write("This is the text series.")

tab1, tab2, tab3 = st.tabs(["DataFrame", "Numeric Series", "Text Series"])

# display_tab_num_content()
with tab1:
    dataframe()
with tab2:
    display_tab_num_content()
with tab3:
    text_series()