# Project COVID-19 in Brazil - Data Analysis

This repository contains an end-to-end project that aims to analyze data on COVID-19 in Brazil. The project involves extracting data from a MySQL database, processing the data using the Pandas library in Python, and generating comprehensive analyses with the help of Power BI.

## Objective
The main objective of this project is to explore and obtain valuable information about COVID-19 death data in Brazil. Through the process of data extraction and analysis, we seek to better understand the evolution of the pandemic, identify trends and patterns, as well as provide insights that can contribute to informed decision-making.

## Technologies Used
- Python: Utilized for data processing, with the Pandas library for data manipulation and analysis.
- MySQL: Involved in extracting data from a MySQL database through SQL queries.
- Power BI: Used for data visualization and the creation of comprehensive analyses, including interactive dashboards, charts, and customized reports.

## Project Structure
The repository is organized as follows:

- extract_cities.py: Python script responsible for extracting data from a CSV file containing all cities in Brazil.
- extract_covid.py: Python script responsible for extracting data from a CSV file downloaded from the MySQL database, containing a sample of COVID-19 data in Brazil.
- transform_covid.py: Python script responsible for transforming data from a CSV file downloaded from the MySQL database, containing a sample of COVID-19 data in Brazil.
- data/raw: Directory that stores the CSV file with the raw data extracted from the MySQL database.
- data/processed: Directory that stores the CSV file with the transformed data ready to be loaded into a data visualization tool.

## Usage
To reproduce or extend the project, follow these steps:
1. Clone this repository to your local machine.
2. Ensure that you have Python (version 3.0 or higher) and Power BI installed in your development environment.
3. Run the extract_cities.py and extract_covid.py scripts to extract data from the CSV files in the data/raw folder.
4. Run the transform_covid.py script to transform and process the data using Pandas.
5. Open the data_analysis.pbix file in Power BI to view the generated analyses and charts.

## Contributing
Contributions are welcome! If you wish to contribute to this project, follow these steps:

1. Fork this repository.
2. Create a new branch for your feature:
3. git checkout -b my-new-feature
4. Make the desired changes and add the modified files:
5. git add .
6. Commit your changes:
7. git commit -m 'Adding my new feature'
8. Push to the branch:
9. git push origin my-new-feature
10. Submit a pull request indicating the changes made and wait for the review.

### License
This project is licensed under the MIT License.

### Contact
If you have any questions or suggestions, feel free to contact:
Demaxsuel Batista
demaxsuelmb@hotmail.com# Covid2019
