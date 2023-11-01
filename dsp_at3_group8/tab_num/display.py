import streamlit as st
import pandas as pd

from tab_num.logics import NumericColumn

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
    instance = NumericColumn(file_path, df)
    instance.find_num_cols()

    select_column = st.selectbox("Which numeric column do you want to explore", instance.cols_list)

    # Based on select_column, generate below data
    instance.set_data(col_name = select_column)

    num = instance.get_summary()
    num_column = pd.DataFrame(num)
    with st.expander ('Overview', expanded = True):
        markdown_text = "<h1 style='text-align: center; font-size: 16px;'>Overview Table</h1>"
        st.markdown(markdown_text, unsafe_allow_html=True)
    #st.write("Numeric Column")
        st.table(num_column)

    instance.set_histogram()
    with st.expander ('Histogram', expanded = True):
        markdown_text = "<h1 style='text-align: center; font-size: 16px;'> Histogram</h1>"
        st.markdown(markdown_text, unsafe_allow_html=True)
    #st.write("**Histogram**")
        #instance.set_histogram()
        st.altair_chart(instance.histogram, use_container_width=True)

    instance.set_frequent()
    with st.expander ('Values Frequency', expanded = True):
        markdown_text = "<h1 style='text-align: center; font-size: 16px;'> Most Frequent Values</h1>"
        st.markdown(markdown_text, unsafe_allow_html=True)

        freq_Data = instance.frequent

    #st.write("**Most Frequent Values**")
        st.dataframe(freq_Data, use_container_width = True)
    