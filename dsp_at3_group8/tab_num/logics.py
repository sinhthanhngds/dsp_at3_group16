import pandas as pd
import altair as alt


class NumericColumn:
    """
    --------------------
    Description
    --------------------
    -> NumericColumn (class): Class that manages a column of numeric data type

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (optional)
    -> df (pd.Dataframe): Pandas dataframe (optional)
    -> cols_list (list): List of columns names of dataset that are numeric type (default set to empty list)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (default set to None)
    -> n_unique (int): Number of unique value of a serie (default set to None)
    -> n_missing (int): Number of missing values of a serie (default set to None)
    -> col_mean (int): Average value of a serie (default set to None)
    -> col_std (int): Standard deviation value of a serie (default set to None)
    -> col_min (int): Minimum value of a serie (default set to None)
    -> col_max (int): Maximum value of a serie (default set to None)
    -> col_median (int): Median value of a serie (default set to None)
    -> n_zeros (int): Number of times a serie has values equal to 0 (default set to None)
    -> n_negatives (int): Number of times a serie has negative values (default set to None)
    -> histogram (alt.Chart): Altair histogram displaying the count for each bin value of a serie (default set to empty)
    -> frequent (pd.DataFrame): Datframe containing the most frequest value of a serie (default set to empty)

    """
    def __init__(self, file_path=None, df=None):
        self.file_path = file_path
        self.df = df
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.col_mean = None
        self.col_std = None
        self.col_min = None
        self.col_max = None
        self.col_median = None
        self.n_zeros = None
        self.n_negatives = None
        self.histogram = alt.Chart()
        self.frequent = pd.DataFrame(columns=['value', 'occurrence', 'percentage'])

    def find_num_cols(self):
        """
        --------------------
        Description
        --------------------
        -> find_num_cols (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.
        Then it will find all columns of numeric data type and store the results in the relevant attribute (self.cols_list).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.df == None:
            if self.file_path != None:
                try:
                    dataframe = pd.read_csv(self.file_path)
                    numeric_df = dataframe.select_dtypes(include=['number']).columns
                    self.cols_list = numeric_df
                    self.df = dataframe
                    print("File loaded successfully!")
                except pd.errors.EmptyDataError:
                    print("The file is empty!")
                except pd.errors.ParserError:
                    print("Error during parsing!")
                except FileNotFoundError:
                    print(f"File {self.file_path} not found!")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                self.df = pd.DataFrame()
        else:
            numeric_df = self.df.select_dtypes(include=['number']).columns
            self.cols_list = numeric_df

    def set_data(self, col_name):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that sets the self.serie attribute with the relevant column from the dataframe and then computes all requested information from self.serie to be displayed in the Numeric section of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> col_name (str): Name of the numeric column to be analysed

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.df.empty is not True:
            self.serie = self.df[col_name]
            self.convert_serie_to_num()
            self.set_frequent()
        self.set_histogram()
        self.get_summary()
        

    def convert_serie_to_num(self):
        """
        --------------------
        Description
        --------------------
        -> convert_serie_to_num (method): Class method that convert a Pandas Series to numeric data type and store the results in the relevant attribute (self.serie).

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.serie.dtype != int or self.serie.dtype != float: 
            try:
                convert_num = self.serie.astype(float).round(4)
            except ValueError:
                convert_num = pd.factorize(self.serie)[0]
            self.serie = convert_num
        

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none and store the results in the relevant attribute (self.cols_list) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if the serie is empty or not

        """
        if self.serie != None or self.serie != "":
            return True
        else:
            return False

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a column and store the results in the relevant attribute (self.n_unique) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            self.n_unique = len(self.serie.unique())

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie and store the results in the relevant attribute (self.n_missing) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            self.n_missing = self.serie.isnull().sum()

    def set_zeros(self):
        """
        --------------------
        Description
        --------------------
        -> set_zeros (method): Class method that computes the number of times a serie has values equal to 0 and store the results in the relevant attribute (self.n_zeros) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            self.n_zeros = self.serie.value_counts().get(0, 0)

    def set_negatives(self):
        """
        --------------------
        Description
        --------------------
        -> set_negatives (method): Class method that computes the number of times a serie has negative values and store the results in the relevant attribute (self.n_negatives) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            self.n_negatives = (self.serie < 0).sum()
        

    def set_mean(self):
        """
        --------------------
        Description
        --------------------
        -> set_mean (method): Class method that computes the average value of a serie and store the results in the relevant attribute (self.col_mean) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            self.col_mean = self.serie.mean()
        

    def set_std(self):
        """
        --------------------
        Description
        --------------------
        -> set_std (method): Class method that computes the standard deviation value of a serie and store the results in the relevant attribute (self.col_std) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            self.col_std = self.serie.std()

    
    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie and store the results in the relevant attribute (self.col_min) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            self.col_min = self.serie.min()

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie and store the results in the relevant attribute (self.col_max) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            self.col_max = self.serie.max()

    def set_median(self):
        """
        --------------------
        Description
        --------------------
        -> set_median (method): Class method that computes the median value of a serie and store the results in the relevant attribute (self.col_median) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            self.col_median = self.serie.median()

    def set_histogram(self):
        """
        --------------------
        Description
        --------------------
        -> set_histogram (method): Class method that computes the Altair histogram displaying the count for each bin value of a serie and store the results in the relevant attribute (self.histogram) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            dataframe = self.serie.to_frame()
            column_name = self.serie.name
            chart = alt.Chart(dataframe[:5000]).mark_bar().encode(
                alt.X(f"{column_name}:Q", bin=True),
                y='count()'
            )
            self.histogram = chart
        else:
            empty_df = pd.DataFrame()
            self.histogram = alt.Chart(empty_df).mark_point()
        

    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie and store the results in the relevant attribute (self.frequent) if self.serie is not empty nor None

        --------------------
        Parameters
        --------------------
        -> end (int):
            Parameter indicating the maximum number of values to be displayed

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.is_serie_none():
            top_20_values = self.serie.value_counts().head(20).index.tolist()
            unique_value_count = []
            unique_value_per = []
            for i in top_20_values:
                count = (self.serie == i).sum()
                percentage = count / self.serie.size
                unique_value_count.append(count)
                unique_value_per.append(percentage)
            self.frequent['value'] = top_20_values
            self.frequent['occurrence'] = unique_value_count
            self.frequent['percentage'] = unique_value_per
        
    def get_summary(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """
        self.set_unique()
        self.set_missing()
        self.set_zeros()
        self.set_negatives()
        self.set_mean()
        self.set_std()
        self.set_min()
        self.set_max()
        self.set_median()
        summary_table = pd.DataFrame(columns = ["Description", "Value"])
        summary_table["Description"] = [
            "Number of Unique Values",
            "Number of Missing Values",
            "Number of Ocurrence of 0 Value",
            "Number of Negative Values",
            "The Average Value",
            "The Standard Deviation Value",
            "The Minimum Value",
            "The Maximum Value",
            "The Median Value"
        ]
        summary_table["Value"] = [
            self.n_unique, 
            self.n_missing, 
            self.n_zeros, 
            self.n_negatives, 
            self.col_mean, 
            self.col_std, 
            self.col_min,
            self.col_max,
            self.col_median 
        ]
        return summary_table
    
    find_num_cols()

