import csv
def read_csv_file(file_path, dtypes:dict):
    """
    Read a CSV file and convert each column to the specified data type.

    Args:
        file_path (str): Path to the CSV data file.
        dtypes (dict): Dictionary mapping column names to data types ('int', 'float', 'string').

    Returns:
        dict: A dictionary where keys are column names and values are lists of column values.
              Missing values (empty strings) are replaced with None.
    
    """
    data = {}
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for column in dtypes:
            data[column] = []

        for row in reader:
            for column in dtypes:
                value = row[column]
                value = value.strip()

                if value == "":
                    data[column].append(None)
                else:
                    # convert the value based on dtypes[column]
                    if dtypes[column] == "int":
                        data[column].append(int(value))
                    elif dtypes[column] == "float":
                        data[column].append(float(value))
                    else:  # assume string
                        data[column].append(value)

    return data

                    

    

def read_dtype(file_path):
    """
    Read a CSV file containing column names and their data types.

    Args:
        file_path (str): Path to the CSV file containing column names and types.

    Returns:
        dict: A dictionary where keys are column names and values are data types ('int', 'float', 'string').
    """
    dtype_dict = {}
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            column_name = row['column'].strip()
            dtype = row['dtype'].strip().lower()
            dtype_dict[column_name] = dtype

    return dtype_dict

def write_file(file_path, data:dict):
    """
    Write a data dictionary to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        data (dict): Dictionary where keys are column names and values are lists of column values.

    Returns:
        None
    """
    columns = list(data.keys())

    if not columns:
        return  # empty data

    num_rows = len(data[columns[0]])

    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(columns)

        for i in range(num_rows):
            row = []
            for col in columns:
                value = data[col][i]
                if value is None:
                    value = ""  # convert None to empty string
                row.append(value)
            writer.writerow(row)

    return
