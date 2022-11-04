# Data analysis file. Contains code to show an example of how you can make data analysis (using pandas for example)

# Import the pandas library
import pandas as pd


def import_data(file_path: str) -> pd.DataFrame:
    # Import the data from the csv file
    data = pd.read_csv(file_path)
    return data


def main():
    # Import the data
    data = import_data("data/copd_1100_train.csv")
    # Print the data
    print(data)


main()