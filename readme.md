# AI Assistant for Data Science

This project is an AI-powered assistant for data science tasks, built with Python, Streamlit, and OpenAI's GPT-3. The assistant can help with exploratory data analysis (EDA), feature engineering, and machine learning model selection.

## Features

- **Data Upload**: Upload your CSV file and the assistant will load it into a Pandas DataFrame.
- **Exploratory Data Analysis**: The assistant can provide an overview of your data, identify missing values, check for duplicates, and calculate correlations between numerical variables.
- **Variable Analysis**: Specify a variable of interest and the assistant will generate a line chart, provide summary statistics, check for normality or specific distribution shapes, assess the presence of outliers, analyze trends, seasonality, and cyclic patterns, and determine the extent of missing values.
- **Feature Engineering Suggestions**: The assistant can suggest new features to create based on the existing data.
- **Business Problem to Data Science Problem**: Input your business problem and the assistant will convert it into a data science problem.
- **Machine Learning Model Selection**: The assistant will suggest suitable machine learning algorithms to solve your data science problem.
- **Python Solution Generation**: The assistant can generate a Python script to solve the data science problem using the selected machine learning algorithm.

## Installation

To install the necessary dependencies for this project, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To start the application, run the following command:

```bash
streamlit run app.py
```

Then, navigate to the URL provided in the terminal to access the application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)