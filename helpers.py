import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, preprocessing, svm
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def input_to_array(brand, series, model, year, power, gear_type, case_type, owner_type, exchange_status, color, repair_status):
    input_arr = pd.read_pickle('line.pkl')
    input_arr['Marka'] = brand
    input_arr['Brand'] = series
    input_arr['Model'] = model
    input_arr['Yil'] = year
    input_arr['Motor Gucu'] = power
    input_arr['Vites'] = gear_type
    input_arr['Kasa Tipi'] = case_type
    input_arr['Kimden'] = owner_type
    input_arr['Durumu'] = exchange_status
    input_arr['Renk'] = color
    input_arr['Hasar Durumu'] = repair_status

    # TODO: Fill the rest of the places for now we are using placeholder values for the rest.


def categorical_columns(df):
    catcolumns = []
    catcolumns = list(df.select_dtypes(include=['object']))
    return catcolumns


def cat_to_num(new_df1, catcolumns):
    new_df2 = []
    new_df2 = new_df1.copy()
    for column in catcolumns:
        label_encoder = LabelEncoder()
        cat = new_df2[column]
        cat_encoded = label_encoder.fit_transform(cat)
        classes = label_encoder.classes_
        encoder = OneHotEncoder()
        cat_1hot = encoder.fit_transform(cat_encoded.reshape(-1,1))
        new_df2 = pd.concat(
            [
                new_df2,
                pd.DataFrame(
                    cat_1hot.toarray(),
                    index=new_df2.index,
                    columns=classes.tolist()
                )
            ],axis=1
        )
        new_df2.drop(column, inplace=True, axis=1)
    return new_df2