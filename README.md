## CSV Explorer Web Application

## Authors
```
** Group 8 - Data Science Practice - University of Technology Sydney **
Sinh Thanh Nguyen - 25099704
Xinhui Wang 	  - 14380428
Siheng Mu 	  - 13475823
Aditi Vyas 	  - 24666152
```


## Description
Our CSV Explorer Web Application was built with the target of making data exploration and analysis way easier for those who do not have fundamental experience in the data-relcated specialisation. It combines interactive dashboards, statistical tools and user-friendly data visualization, although does not require any complicated program installed or in-depth training.

##### Limitation
Despite its robustness and convenience, our application is currently facing up with the following limitations:
- File size limitation: CSV files can vary greatly in size, while our application has a maximum file upload limit of 200MB.
- Data Import Compatibility: our application could not handle all CSV variations, and issues with delimiters, encoding, or file formats may arise during importing operations.
- Lack of Advanced Analysis Tools: While the application can help with basic data manipulation, it does not offer advanced statistical analysis or machine learning capabilities, which might be required for in-depth data analysis.


##### Future improvement:
Because of the ever-increasing demand for instant, advanced and multitasking applications, the following functionalities could be considered to be appended to our CSV Explorer:
- Advanced Data Visualization: Incorporate advanced charting and graphing capabilities to enable users to visualize data trends and patterns more effectively. Support a wide range of chart types (e.g., bar charts, scatter plots, heatmaps) to cater to diverse data needs.
- Data Transformation Tools: Enhance the application with powerful data transformation features, including the ability to merge, split, and pivot columns, apply mathematical operations, and create calculated fields.
- Machine Learning Integration: Incorporate machine learning and predictive analytics capabilities for advanced data analysis and pattern recognition.
- User Feedback Mechanism: Implement a feedback system that allows users to suggest improvements and report issues directly from within the application.


## How to Setup
Our web application was supported by the following environment and packages. Please make sure they have been installed with the specific versions:
```
	* Python: 3.9.13
	* Streamlit: 1.13.0
	* Altair: 4.2.0
	* Pandas: 2.0.3
```
Application installation on local machine was taken as below (command prompt), with the assumption that you would install the application at "installation_directory":
On terminal:
```
cd [installation_directory]
```
```
git clone git@github.com:sinhthanhngds/dsp_at3_group8.git
```
The terminal will show whether the installation is successful


## How to Run the Program
To run the program:
On terminal:
```
cd
```
```
cd [installation_directory]/dsp_at3_group8/dsp_at3_group8/app
```
```
streamlit run streamlit_app.py
```
The application webpage should show up. Simply upload your .csv file and start.
## Project Structure
Folders structures:
```
dsp_at3_group8/
├── README.md: project description
├── .gitignore: ignore changes in .DS_Store and __pycache__
├── .gitattributes
├── dsp_at3_group8/
│   ├── requirements.txt
│   ├── app/
│   │	├── streamlit_app.py: codes for .csv file upload and calling to relevant functions
│   │	├── __init__.py
│   ├── tab_df/
│   │	├── __init__.py
│   │	├── logics.py: calculates and stores overall dataframe information to be displayed
│   │   ├── display.py: displays information stored in logics.py
│   ├── tab_num/
│   │	├── __init__.py
│   │	├── logics.py: extractss, calculates and stores numerical column information
│   │	├── display.py: numerical column selection and display information stored in logics.py
│   ├── tab_text/
│   │	├── __init__.py
│   │	├── logics.py: extracts, calculates and stores objects column information
│   │   ├── display.py: text column selection and display information stored in logics.py
│   ├── tab_date/
│   │	├── __init__.py
│   │	├── logics.py: extracts, calculates and store information of selected date-time column
│   │	├── display.py: datetime column selection and display information stored in logics.py
```



## Citations
<Mention authors and provide links code you source externally>
    