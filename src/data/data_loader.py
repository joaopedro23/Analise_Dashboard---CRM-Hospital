import pandas as pd
import pathlib

def load_data():
    BASE_PATH = pathlib.Path(__file__).parent.parent.parent.resolve()
    DATA_PATH = BASE_PATH.joinpath("data").resolve()
    df = pd.read_csv(DATA_PATH.joinpath("clinical_analytics.csv"))

    clinic_list = df["Clinic Name"].unique()
    df["Admit Source"] = df["Admit Source"].fillna("Not Identified")
    admit_list = df["Admit Source"].unique().tolist()

    df["Check-In Time"] = pd.to_datetime(df["Check-In Time"], format='%Y-%m-%d %I:%M:%S %p')

    df["Days of Wk"] = df["Check-In Time"].dt.strftime("%A")
    df["Check-In Hour"] = df["Check-In Time"].dt.strftime("%I %p")

    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return df, clinic_list, admit_list, day_list
