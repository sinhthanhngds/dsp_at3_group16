import streamlit as st

from tab_text.logics import TextColumn

def display_tab_text_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_text_content (function): Function that will instantiate tab_text.logics.TextColumn class, save it into Streamlit session state and call its tab_text.logics.TextColumn.find_text_cols() method in order to find all text columns.
    Then it will display a Streamlit select box with the list of text columns found.
    Once the user select a text column from the select box, it will call the tab_text.logics.TextColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_text.logics.TextColumn.get_summary() as a Streamlit Table
    - the graph from tab_text.logics.TextColumn.histogram using Streamlit.altair_chart()
    - the results of tab_text.logics.TextColumn.frequent using Streamlit.write
 
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
    # Instantiate the TextColumn class
    text_col_instance = TextColumn(file_path=file_path, df=df)
    
    # Find text columns
    text_col_instance.find_text_cols()
    
    # Display a Streamlit select box for text columns
    selected_text_column = st.selectbox("Select a text column:", text_col_instance.cols_list)
    
    # Compute the necessary data for the selected column
    text_col_instance.set_data(selected_text_column)
    
    # Display the results in a Streamlit Expander container
    with st.expander("Data Overview", expanded = True):
        # Display the summary as a Streamlit table
        markdown_text = "<h1 style='text-align: center; font-size: 16px;'>Overview</h1>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.table(text_col_instance.get_summary().astype ('str'))
    with st.expander('Histogram', expanded = True):
        # Display the histogram using Streamlit's altair_chart
        markdown_text = "<h1 style='text-align: center; font-size: 16px;'>Histogram</h1>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.altair_chart(text_col_instance.barchart, use_container_width=True)
    with st.expander ('Data Frequency', expanded = True):   
        # Display the frequent values using Streamlit's write
        markdown_text = "<h1 style='text-align: center; font-size: 16px;'>Data Frequency</h1>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.write(text_col_instance.frequent, use_container_width= True)

    
