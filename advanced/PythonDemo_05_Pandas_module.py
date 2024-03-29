# This file provides demo for pandas functionality
import random

import pandas as pd


def seriesDemo():
    """This function gives demo for Pandas Series"""
    a = [1, 2.2, "Pooja", 4, 5]
    s1 = pd.Series(a, index=["id", "module_num", "name", "n1", "n2"])
    print("Series before update\n", s1)
    s1.loc[0] = 2
    s1.iloc[3:5] = 12
    s1._set_value("n1", 15)
    s1['name'] = 'Mrs. Pooja'
    print("Series before update")
    print(s1)

    d1 = {'c1': 'India', 'c2': 'USA', 'c3': 'Switzerland'}
    print("Dictionary: ", d1)
    s2 = pd.Series(d1, name='Country')
    print(f"Series: {s2.name} Data Type: {s2.dtype} Size: {s2.size} \n")
    print(s2)

    arr = [1, 2, 3, 4]
    arr2 = [10, 20, 30, 4]
    s3 = pd.Series(arr)
    s4 = pd.Series(arr2)
    s5 = pd.concat([s3, s4], ignore_index=True)
    s5.name = "S5"
    print(s5.drop(labels=2))
    print("Index where value 4 is present : \n ", s5.loc[s5 == 4])


def dataFrameDemo():
    d1 = {
        "id": [1, 2, 3],
        "name": ["Rohit", "Pooja", "Rajani"]
    }
    print(f"Type of d1: {type(d1)}")
    df = pd.DataFrame(d1)
    print(df)
    print("-" * 25)

    d2 = [10, 20, 30, 40]
    df2 = pd.DataFrame(d2, index=['first', 'second', 'third', 'fourth'], columns=['id'])
    print("using iloc with index \n", df2.iloc[1])
    print("using loc with label index \n", df2.loc['fourth'])
    print("/" * 15)

    print("using iloc with multiple rows \n", df2.iloc[[0, 2]])
    print("using loc with multiple rows \n", df2.loc[['second', 'fourth']])
    print("/" * 15)

    print("using iloc slicing \n", df2.iloc[:2])
    print("using loc slicing \n", df2.loc['third':'fourth'])
    print("-" * 25)

    d3 = [random.randint(i, i * 10) for i in range(0, 500)]
    d4 = ['A', 'B', 'C', 'D', 'E'] * 100

    s3, s4 = pd.Series(d3), pd.Series(d4)

    df1 = pd.concat([s3, s4], axis=1).rename(columns={0: 'id', 1: 'str_val'})
    print(df1[['id', 'str_val']][10:20])
    print("-" * 25)


def dataframe_filter_demo():
    """Dataframe operation"""

    d3 = [random.randint(i, i * 10) for i in range(0, 500)]
    d4 = ['A', 'B', 'C', 'D', 'E'] * 100

    s3, s4 = pd.Series(d3), pd.Series(d4)

    df1 = pd.concat([s3, s4], axis=1).rename(columns={0: 'id', 1: 'str_val'})

    for x in df1.index:
        if df1.loc[x, 'id'] % 500 == 0:
            print(df1.loc[x]['id'])

    print("Single column condition: \n", df1.loc[df1['str_val'] == 'A'])
    print("-" * 25)

    print("Double column condition: \n", df1.loc[(df1['str_val'] == 'A') & (df1['id'] % 10 == 0)])
    print("-" * 25)

    print(df1.query("str_val == 'B' and (id > 110 and id < 700)"))

    print(df1.filter(items=['id', 'str_val']).head(20))

    print(df1.filter(like='val').head(20))


def dataframe_duplicate_demo():
    d = {
        'id': [1, 2, 3, 4, 5, 1],
        'name': ['R', 'O', 'H', 'I', 'T', 'R']
    }
    df = pd.DataFrame(d)
    print("Input data frame: ", df)

    duplicated_series = df.duplicated()

    print("Find duplicate rows \n", duplicated_series)

    print("Find only duplicated row \n", df[duplicated_series == 1])

    print("Remove duplicate rows \n", df.drop_duplicates())

    print("Remove duplicate on basis of column values \n", df.drop_duplicates(subset=['name']))

    print("update duplicated values in df")
    for i in df[duplicated_series == 1].index.values:
        df.loc[i] = (6, 'P')

    print(df)


def null_handling_demo():
    d = {
        'id': [1, 2, 3, 4, 5, None, 8],
        'name': ['R', 'O', 'H', 'I', 'T', 'C', None]
    }
    df = pd.DataFrame(d)

    print("Data frame with null")
    print(df.isna())

    print("Remove null values from data frame")
    df1 = df.dropna()
    df2 = pd.concat([pd.to_numeric(df1['id'], downcast="integer"), df1['name']], axis=1)
    print(df2)

    print("Fill null values from data frame")
    d1 = {'id': 0, 'name': '#'}
    df1 = df.fillna(d1).astype(dtype={'id': int, 'name': object})
    print(df1)


def dataframe_add_rows():
    d = {
        'id': [1, 2, 3, 4, 5],
        'name': ['R', 'O', 'H', 'I', 'T']
    }
    df = pd.DataFrame(d)

    # to add single row
    df.loc[df.index.max() + 1] = (6, 'P')

    # to add multiple rows
    multiple_rows = {
        'id': [7, 8, 9, 10, 11, 12],
        'name': ['R', 'A', 'K', 'A', 'S', 'H']
    }
    df1 = pd.DataFrame(multiple_rows)
    df = pd.concat([df, df1], axis=0, ignore_index=True)
    print(df)


def dataframe_where_demo():
    d = {
        'id': [1, 2, 3, 4, 5],
        'name': ['R', 'O', 'H', 'I', 'T']
    }
    df = pd.DataFrame(d)

    cond1 = df['id'] > 2
    cond2 = df['name'] != 'T'

    print(df.where(cond1 & cond2))


def dataframe_remove_rows():
    d = {
        'id': [1, 2, 3, 4, 5],
        'name': ['R', 'O', 'H', 'I', 'T']
    }
    df = pd.DataFrame(d)

    index_list = df.index.values

    print("Remove first two elements from dataframe using indexes")
    print(df.drop(index=index_list[:2]))

    print("Remove elements from dataframe on basis of condition")
    df.drop(df[df['id'] == 2].index.values, inplace=True)
    print(df)

    print("Remove column id from dataframe")
    df.drop(columns=['id'], inplace=True)

    print(df)


def dataframe_join_demo():
    emp_data = {
        'emp_id': [10, 20, 30, 40, 50, 60],
        'emp_name': ["Rohit", "Pooja", "Rajani", "Rushi", "Rutu", "Prithvi"],
        'emp_sal': [5600, 6200, 7900, 7623.45, 5823.41, 5399.14],
        'dept_id': [1, 2, 3, 1, 3, 3]
    }

    dept_data = {
        'dept_id': [1, 2, 3],
        'dept_name': ["IT", "Civil", "Computer Science"]
    }

    emp_df = pd.DataFrame(emp_data)
    dept_df = pd.DataFrame(dept_data)
    print("Emp df \n", emp_df)
    print("Dept df \n", dept_df)

    print("Joined df")
    print(emp_df.join(dept_df.set_index('dept_id'), on='dept_id', how='inner'))

    dept_renamed_df = dept_df.rename(columns={'dept_id': 'id'})
    print(dept_renamed_df)
    # print(emp_df.join(dept_renamed_df.set_index('id'), on='id', how='inner'))


def dataframe_merge_demo():
    emp_data = {
        'emp_id': [10, 20, 30, 40, 50, 60],
        'emp_name': ["Rohit", "Pooja", "Rajani", "Rushi", "Rutu", "Prithvi"],
        'emp_sal': [5600, 6200, 7900, 7623.45, 5823.41, 5399.14],
        'dept_id': [1, 2, 3, 1, 3, 3]
    }

    dept_data = {
        'id': [1, 2, 3],
        'dept_name': ["IT", "Civil", "Computer Science"]
    }

    emp_df = pd.DataFrame(emp_data)
    dept_df = pd.DataFrame(dept_data)

    print("Merged df when column name is not same")
    print(emp_df.merge(dept_df, how='left', left_on='dept_id', right_on='id'))

    print("Merged df when column names are same")
    print(emp_df.merge(dept_df.rename(columns={'id': 'dept_id'}), how='left'))


dataframe_remove_rows()
