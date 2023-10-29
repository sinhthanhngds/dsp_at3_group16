import streamlit as st

from tab_df.logics import Dataset

def display_tab_df_content(file_path):
    """
    --------------------
    Description
    --------------------
    -> display_overall_df (function): Function that will instantiate tab_df.logics.Dataset class, save it into Streamlit session state and call its tab_df.logics.Dataset.set_data() method in order to compute all information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    1. the results of tab_df.logics.Dataset.get_summary() as a Streamlit Table
    2. the results of tab_df.logics.Dataset.table using Streamlit.write()
    Finally it will display a second Streamlit Expander container with a slider to select the number of rows to be displayed and a radio button to select the method (head, tail, sample).
    According to the values selected on the slider and radio button, display the subset of the dataframe accordingly using Streamlit.dataframe
    
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file

    --------------------
    Returns
    --------------------
    -> None
    
    """
    st.session_state.dataset = Dataset (file_path)
    st.session_state.dataset.set_data()
    st.table (st.session_state.dataset.get_summary())
    st.write (st.session_state.dataset.table.astype ('str'))
    num_rows = st.slider ('Select number of rows to display',min_value = 1, max_value = 50)
    method = st.radio (
        'Select method',
        ['Head', 'Tail', 'Sample']
    )
    if method == 'Head':
        st.write (st.session_state.dataset.get_head(num_rows))
    elif method == 'Tail':
        st.write (st.session_state.dataset.get_tail(num_rows))
    else:
        st.write (st.session_state.dataset.get_sample (num_rows))
    


