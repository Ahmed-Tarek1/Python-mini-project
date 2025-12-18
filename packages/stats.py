from functools import reduce

def is_numeric_col(col: list) -> bool:
    """Check if a column contains only numeric values (ignoring None)."""
    filtered_col = list(filter(lambda x: x is not None, col))
    return all(isinstance(x, (int, float)) for x in filtered_col)

def get_col_max(col:list):
    """
    Compute the maximum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The maximum value in the column (numeric type).
    """
    if not is_numeric_col(col):
        return None
    
    filtered_col = list(filter(lambda x: x is not None, col))
    
    if not filtered_col:  # If no valid numbers, return None
        return None

    # Use reduce to compute maximum
    return reduce(lambda a, b: a if a > b else b, filtered_col)
    #return reduce(lambda a, b: a if a > b else b, (x for x in col if x is not None)) if is_numeric_col(col) and any(x is not None for x in col) else None


def get_col_min(col:list):
    """
    Compute the minimum value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The minimum value in the column (numeric type).
    """
    if not is_numeric_col(col):
        return None
    
    filtered_col = list(filter(lambda x: x is not None, col))

    if not filtered_col:
        return None
    
    return reduce(lambda a, b: a if a < b else b, filtered_col)
    #return reduce(lambda a, b: a if a < b else b, (x for x in col if x is not None)) if is_numeric_col(col) and any(x is not None for x in col) else None


def get_col_mean(col:list):
    """
    Compute the mean (average) value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The mean value of the column (float).
    """
    if not is_numeric_col(col):
        return None
    
    filtered_col = list(filter(lambda x: x is not None, col))

    if not filtered_col:
        return None
    
    total = reduce(lambda a, b: a + b, filtered_col)
    count = len(filtered_col)
    
    return total / count

def get_col_median(col:list):
    """
    Compute the median value of a numerical column.

    Args:
        col (list): A list of numerical values. `None` values are ignored.

    Returns:
        The median value of the column (numeric type).
    """
    if not is_numeric_col(col):
        return None
    
    filtered_col = list(filter(lambda x: x is not None, col))

    if not filtered_col:
        return None
    
    n = len(filtered_col)
    sorted_col = sorted(filtered_col)

    if n % 2 == 0:
        return (sorted_col[n//2 - 1] + sorted_col[n//2]) / 2
    else:
        return sorted_col[n//2]
    
def get_col_mode(col:list):
    """
    Compute the mode (most frequent value) of a column.

    Args:
        col (list): A list of values. `None` values are ignored.

    Returns:
        The mode value of the column. If multiple values have the same
        frequency, the first encountered is returned.
    """
    filtered_col = list(filter(lambda x: x is not None, col))

    if not filtered_col:
        return None
    
    freq = {}
    for val in filtered_col:
        freq[val] = freq.get(val, 0) + 1
    mx_cnt = -1
    mode_val = None

    for val in filtered_col:
        cnt = freq.get(val)
        if cnt > mx_cnt:
            mx_cnt = cnt
            mode_val = val
    
    return mode_val
    
def get_stat(data:dict, dtypes:dict, function:str):
    """
    Apply a statistical function to all numerical columns in a dataset.

    Args:
        data (dict): Dictionary where keys are column names and values are lists of column values.
        dtypes (dict): Dictionary where keys are column names and values are data types ('int', 'float', 'string').
        function (function): A function to apply to each numerical column (e.g., get_col_max, get_col_mean).

    Returns:
        dict: A dictionary where keys are column names and values are the result
        of applying the function to that column. Only numerical columns are processed.
    """
    res = {}
    for col_name, col_values in data.items():
        if dtypes.get(col_name) in ('int', 'float') and is_numeric_col(col_values):
            res[col_name] = function(col_values)

    return res






