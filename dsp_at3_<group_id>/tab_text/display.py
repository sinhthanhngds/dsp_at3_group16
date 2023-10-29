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
    st.session_state.text_column = TextColumn (df = df)
    st.session_state.text_column.find_text_cols()
    st.session_state.selected_text_col = st.selectbox ('Which text column do you want to analyze', st.session_state.text_column.cols_list)
    st.session_state.text_column.set_data (st.session_state.selected_text_col)
    st.table (st.session_state.text_column.get_summary())
    st.altair_chart(st.session_state.text_column.barchart)
    st.table (st.session_state.text_column.frequent)





    