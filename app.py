import json
import pandas as pd

def handler(event, context):

    df = pd.DataFrame([1,2,3])
    print(df)
    return "hola"