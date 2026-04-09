# ParisMetro
SIA Project - Income analysis of Paris Metro lines using spatial data

## Structure 
The project has the following folder structure:

- Data:         Contains the cropped and reprojected income raster
- Functions:    Contains the functions to load data, do spatial and raster analysis 
- Notebook:     Contains the jupyter notebook
- Outputs:      Contains the output figures, tables and HTML maps
- Requirements: Contains the required environment and packages

## Description
The script creates 400m catchment buffer around paris metro stations and analyze the average income inside them. For the analysis, several steps conducted: 

1. Introduction and Context
2. Imports
3. Data Processing
4. Data Analysis
    4.1 Income Distribution
    4.2 Grouping Stations per Line 
    4.3 Income per Line
    4.4 Inequality per Line
5. Regression for Line X
    5.1 Regression North
    5.2 Regression South
6. Sensitivity Analysis
7. Conclusion 

## Set-Up
To run the code, Open the notebook in the notebook/ folder and run all cells.
please install the packages indicated in the requirements file

```bash
pip install -r requirements/requirements.txt
