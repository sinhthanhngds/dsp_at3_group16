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
    data = Dataset(file_path)
    data.set_df()
    data.set_columns()
    data.set_dimensions()
    data.set_duplicates()
    data.set_missing()
    ds_summary = data.get_summary()
    ds_table = data.set_table()
    
    with st.expander("DataFrame"):
        st.table(ds_summary)
        st.table(ds_table)
    
    with st.expander("Explore DataFrame"):
        n = st.slider(
            'Select the number of rows to be displayed',
            min_value=5,
            max_value=50,
            value=5)
        
        option = st.radio(
        'Exploration Method',
        ["Head", "Tail", "Sample"]
        )
        
        if option == "Head":
            st.title(
                "Top Rows of Selected Table"
                )
            ds_head = data.get_head(n)
            st.write(ds_head)
        elif option == "Tail":
            st.title(
                "Bottom Rows of Selected Table"
                )
            ds_tail = data.get_tail(n)
            st.write(ds_tail)
        elif option == "Sample":
            st.title(
                "Sample Rows of Selected Table"
                )
            ds_sample = data.get_sample(n)
            st.write(ds_sample)
