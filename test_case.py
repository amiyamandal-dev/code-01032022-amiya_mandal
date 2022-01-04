import unittest

import pandas as pd
from fastapi.testclient import TestClient

from utils import process_result
from app import app

client = TestClient(app)


class TestBmiMethods(unittest.TestCase):

    def test_process_result(self):
        d = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
             {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
             {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
             {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
             {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
             {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
        df = pd.DataFrame(d)
        final_df = process_result(df)
        result_val = [32.83, 32.79, 23.77, 22.5, 31.11, 29.40]
        for index_val, i in final_df.iterrows():
            self.assertEqual(i["bmi"], result_val[index_val])


def test_api():
    response = client.post("/api/bmi/", json={"data": [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                                                       {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                                                       {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                                                       {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                                                       {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                                                       {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]}
                           )
    assert response.status_code == 201
    assert response.json() == {
        "data": [
            {
                "HeightCm": 171,
                "Gender": "Male",
                "WeightKg": 96,
                "bmi": 32.83,
                "BMI Category": "Moderately obese",
                "Health risk": "Medium risk"
            },
            {
                "HeightCm": 161,
                "Gender": "Male",
                "WeightKg": 85,
                "bmi": 32.79,
                "BMI Category": "Moderately obese",
                "Health risk": "Medium risk"
            },
            {
                "HeightCm": 180,
                "Gender": "Male",
                "WeightKg": 77,
                "bmi": 23.77,
                "BMI Category": "Normal weight",
                "Health risk": "Low risk"
            },
            {
                "HeightCm": 166,
                "Gender": "Female",
                "WeightKg": 62,
                "bmi": 22.5,
                "BMI Category": "Normal weight",
                "Health risk": "Low risk"
            },
            {
                "HeightCm": 150,
                "Gender": "Female",
                "WeightKg": 70,
                "bmi": 31.11,
                "BMI Category": "Moderately obese",
                "Health risk": "Medium risk"
            },
            {
                "HeightCm": 167,
                "Gender": "Female",
                "WeightKg": 82,
                "bmi": 29.4,
                "BMI Category": "Overweight",
                "Health risk": "Enhanced risk"
            }
        ]
    }


if __name__ == '__main__':
    unittest.main()
    test_api()
