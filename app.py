from enum import Enum
from typing import List

import pandas as pd
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utils import process_result

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Gender(str, Enum):
    male = 'Male'
    female = 'Female'


class SubModel(BaseModel):
    HeightCm: float
    Gender: Gender
    WeightKg: float


class MainModel(BaseModel):
    data: List[SubModel]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/bmi/", status_code=status.HTTP_201_CREATED)
def process_bmi(data: MainModel):
    list_data = data.dict()["data"]
    df = pd.DataFrame(list_data)
    final_df = process_result(df)
    return {"data": final_df.to_dict("records")}
