import numpy as np
import pandas as pd


def weight_status(series) -> (str, str):
    if series["bmi"] == np.inf:
        return "Wrong Data", "Wrong Data"
    elif series["bmi"] <= 18.4:
        return "Underweight", "Malnutrition risk"
    elif 24.9 >= series["bmi"] >= 18.5:
        return "Normal weight", "Low risk"
    elif 29.9 >= series["bmi"] >= 25:
        return "Overweight", "Enhanced risk"
    elif 34.9 >= series["bmi"] >= 30:
        return "Moderately obese", "Medium risk"
    elif 34.9 >= series["bmi"] >= 30:
        return "Severely obese", "High risk"
    elif series["bmi"] >= 40:
        return "Very severely obese", "Very high risk"


def process_result(df_to_process: pd.DataFrame):
    try:
        df_to_process["HeightM_sqr"] = df_to_process["HeightCm"] ** 2 / 100 ** 2
        df_to_process["bmi"] = df_to_process["WeightKg"] / df_to_process["HeightM_sqr"]
        df_to_process["bmi"] = df_to_process["bmi"].round(2)
        df_to_process["BMI Category"], df_to_process["Health risk"] = df_to_process.apply(weight_status, axis=1,
                                                                                          result_type='expand').T.values
        del df_to_process["HeightM_sqr"]
        return df_to_process
    except Exception as e:
        print(e)
