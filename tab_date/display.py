import streamlit as st

from tab_date.logics import DateColumn

def display_tab_date_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_date_content (function): Function that will instantiate tab_date.logics.DateColumn class, save it into Streamlit session state and call its tab_date.logics.DateColumn.find_date_cols() method in order to find all datetime columns.
    Then it will display a Streamlit select box with the list of datetime columns found.
    Once the user select a datetime column from the select box, it will call the tab_date.logics.DateColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_date.logics.DateColumn.get_summary() as a Streamlit Table
    - the graph from tab_date.logics.DateColumn.histogram using Streamlit.altair_chart()
    - the results of tab_date.logics.DateColumn.frequent using Streamlit.write
 
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
    st.session_state.date_column = DateColumn(df = df)
    st.session_state.date_column.find_date_cols()
    st.session_state.selected_date_col = st.selectbox ('What date time column do you want to explore?', st.session_state.date_column.cols_list)
    st.session_state.date_column.set_data(st.session_state.selected_date_col)
    if 'datetime' in str(st.session_state.date_column.serie.dtype):
        with st.expander ('Overview', expanded = True):
            markdown_text = "<h1 style='text-align: center; font-size: 16px;'>Overview Table</h1>"
            st.markdown(markdown_text, unsafe_allow_html=True)
            st.table (st.session_state.date_column.get_summary())
        with st.expander ('Frequency Histogram', expanded = True):
            st.altair_chart(st.session_state.date_column.barchart, use_container_width=True)
        with st.expander ('Frequency Report', expanded = True):
            markdown_text = "<h1 style='text-align: center; font-size: 16px;'>Most Frequent Values</h1>"
            st.markdown(markdown_text, unsafe_allow_html=True)
            st.table (st.session_state.date_column.frequent)
    else:
        st.warning ('Please select a data-time like column', icon = '😅')
    