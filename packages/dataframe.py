from .file_handler import *
from .stats import *
from typing import Callable

class Dataframe:
    def __init__(self, data: dict, dtype: dict):
        self.data = data     
        self.dtype = dtype
    
    #TODO: define read_csv(data_path, dtype_path)
    @classmethod
    def read_csv(cls, data_path, dtype_path):
        dtype = read_dtype(dtype_path)
        data = read_csv_file(data_path, dtype)
        return  cls(data, dtype)
    
    #TODO: define count_nulls()
    def count_nulls(self):
        res = {}
        for name, values in self.data.items():
            cnt = 0
            for val in values:
                if val is None:
                    cnt += 1

            res[name] = cnt

        return res
    
    #TODO: define describe()
    def describe(self, path: str = "data/describe.csv"):
        stats_rows = {
        "column": [],
        "nulls": [],
        "max": [],
        "min": [],
        "mean": [],
        "median": [],
        "mode": []
        }

        nulls = self.count_nulls()
        for col_name, values in self.data.items():
            stats_rows["column"].append(col_name)
            stats_rows["nulls"].append(nulls[col_name])
            stats_rows["max"].append(get_col_max(values))
            stats_rows["min"].append(get_col_min(values))
            stats_rows["mean"].append(get_col_mean(values))
            stats_rows["median"].append(get_col_median(values))
            stats_rows["mode"].append(get_col_mode(values))

        write_file(path, stats_rows)
        return
    
    #TODO: define fillna()   
    def fillna(self, num_strategy: Callable, cat_strategy: Callable):
        for col_name, values in self.data.items():

            if (self.dtype[col_name] in ('int', 'float')):
                fill_val = num_strategy(values)
            else:
                fill_val = cat_strategy(values)

            for i, val in enumerate(values):
                if val is None:
                    values[i] = fill_val
                    
        return

    #TODO: define to_csv()
    def to_csv(self, path: str = "data/out.csv"):
        write_file(path, self.data)
        return