# Data analysis file. Contains code to show an example of how you can make data analysis (using pandas for example)

# Import the pandas library
import pandas as pd


def import_data(file_path: str) -> pd.DataFrame:
    # Import the data from the csv file
    data = pd.read_csv(file_path)
    return data


def extract_lines_by_label(data: pd.DataFrame, label: int) -> pd.DataFrame:
    # Extract the lines with the column "label" equal to the label parameter
    return data[data['Label'] == label]


def main():
    # Import the data
    data = import_data("data/copd_1100_train.csv")
    
    # Extract the lines with the label 4
    data = extract_lines_by_label(data, 4)

    # Print the data
    print(data)


main()