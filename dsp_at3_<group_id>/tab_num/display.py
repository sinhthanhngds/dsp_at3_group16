import streamlit as st

from tab_num.logics import NumericColumn

def display_tab_num_content(df = None, file_path=None):
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
    st.session_state.num_column = NumericColumn(df = df)
    st.session_state.num_column.find_num_cols()
    col = st.selectbox ('Which column do you want to explore', st.session_state.num_column.cols_list)
    st.session_state.num_column.set_data(col)
    st.table (st.session_state.num_column.get_summary())
    st.altair_chart(st.session_state.num_column.histogram)
    st.table (st.session_state.num_column.frequent)
    


    