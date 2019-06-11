# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from pprint import pprint


def handling_violation():
    data_return = {}
    df = pd.read_csv('data_crawl/violation.txt', sep=",", header=None,
                     names=["stt", "number", "type", "error", "time", "address"])
    df.fillna(value='0')

    df['timeStamp'] = pd.to_datetime(df['time'])
    df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
    df['Month'] = df['timeStamp'].apply(lambda time: time.month)
    df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
    df['Day'] = df['timeStamp'].apply(lambda time: time.day)
    df['year'] = df['timeStamp'].apply(lambda time: time.year)

    # error with hour
    data_return["_hour"] = df.groupby([df['Hour']])['error'].count().to_dict()

    # error with day of week
    data_return["_day"] = df.groupby([df['Day of Week']])[
        'error'].count().to_dict()

    # couting error following the type of vehicle
    data_return["_type"] = df['type'].value_counts().to_dict()

    return data_return


def handling_random():
    data_return = {}
    data_path = "data_crawl/statistic_random_number.txt"
    header = ["BS", "Recent_Day", "Sum_Of_Appearance", "Not_Return"]
    df = pd.read_csv(data_path, sep=",", header=None, names=header)

    df_sort = df.sort_values("Sum_Of_Appearance")['Sum_Of_Appearance']
    data_return["_most"] = df_sort.tail(10).to_dict()
    data_return["_least"] = df_sort.head(10).to_dict()

    return data_return


pprint(handling_violation())
pprint(handling_random())
