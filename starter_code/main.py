from packages.dataframe import *
def main():
    # TODO: Read data
    ob = Dataframe()
    df = ob.read_csv("/Users/ahmedtarek/Downloads/ITI/Python for ML/Mini Project/starter_code/data/titanic.csv", "/Users/ahmedtarek/Downloads/ITI/Python for ML/Mini Project/starter_code/data/titanic_dtype.csv")

    # TODO: Fill missing values
    # Numeric columns → mean
    # Categorical columns → mode
    df.fillna('get_col_mean', 'get_col_mode')

    # TODO:Generate statistics file
    df.describe()

    # TODO:Write cleaned data to CSV
    df.to_csv()


if __name__ == "__main__":
    main()
