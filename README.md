# <project title>

## Authors
Group <group number> : 
- <first and last name> (<UTS student id>)
- <first and last name> (<UTS student id>)
- <first and last name> (<UTS student id>)

## Description
<What your application does>
- Our CSV Explorer Web Application was built with the target of making data exploration and analysis way easier who those who do not have fundamental experience in the field of data. It combines interactive dashboards, statistical tools and user-friendly data visualization, although does not require any complicated program installed or in-depth training.

- Similar to any application developing team, we also faced up with a limited number of challenges, namely, coding inconsistency, packages limitation and versional conflicts.

The application was contributed by 4 developers that came from different backgrounds. We have different coding experience, knowledge and methods to deal with data. Moreover, functions on our application are strictly related to each other. As the result, conflicts and errors raised, leading to a large amount of time to resolve.

Regarding imported libraries and packages, we installed them with particular versions mentioned in 'requirements.txt'. However, there were also conflicts between those libraries when we were implementing our codes, which could be caused by packages loss during installation.

- Future improvement:
	+ Advanced Data Visualization: Incorporate advanced charting and graphing capabilities to enable users to visualize data trends and patterns more effectively. Support a wide range of chart types (e.g., bar charts, scatter plots, heatmaps) to cater to diverse data needs.
	+ Data Transformation Tools: Enhance the application with powerful data transformation features, including the ability to merge, split, and pivot columns, apply mathematical operations, and create calculated fields.
	+ Machine Learning Integration: Incorporate machine learning and predictive analytics capabilities for advanced data analysis and pattern recognition.
	+ User Feedback Mechanism: Implement a feedback system that allows users to suggest improvements and report issues directly from within the application.


## How to Setup
-------------Installation-----------
Our web application was supported by the following environment and packages. Please make sure they have been installed with the specific versions:
	+ Python: 3.9.13
	+ Streamlit: 1.13.0
	+ Altair: 4.2.0
	+ Pandas: 2.0.3
Application installation on local machine was taken as below (command prompt), with the assumption that you would install the application at "installation_directory":
On terminal:
+ cd [installation_directory]
+ git clone git@github.com:sinhthanhngds/dsp_at3_group8.git
The terminal will show whether the installation is successful


## How to Run the Program
To run the program:
On terminal:
+ cd
+ cd [installation_directory]/dsp_at3_group8/dsp_at3_group8/app
+ streamlit run streamlit_app.py
The application webpage should show up. Simply upload your .csv file and start.

## Project Structure
<List all folders and files of this project and provide quick description for each of them>
Folders structures:
dsp_at3_group8 ---app ---- __init__.py
	       |      \---  streamlit_app.py: contains codes for .csv file upload and calling to 	       |	                              relevant functions
	       |--tab_df --- __init__.py	
               |         \--- display.py: displays information stored in logics.py
	       |          \--- logics.py: calculates and stores overall dataframe description to be 	       |				  displayed
               |--tab_num --- __init__.py
               |          \--- display.py: displays information stored in logics.py
               |           \--- logis.py: calculates and stores numerical data description to be               	       |				  displayed
               |--tab_text --- __init__.py
               |          \--- display.py: displays information stored in logics.py
               |           \--- logis.py: calculates and stores object columns information to be 	       |					displayed
	       |--tab_date --- __init__.py
               |          \--- display.py: displays information stored in logics.py
               |           \--- logis.py: calculates and stores information about datetime columns to 					  be displayed




## Citations
<Mention authors and provide links code you source externally>
