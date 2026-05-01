import os
import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_object


def predict_from_data(input_df: pd.DataFrame):
    try:
        preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
        model_path = os.path.join('artifacts', 'model.pkl')

        preprocessor = load_object(preprocessor_path)
        model = load_object(model_path)

        input_arr = preprocessor.transform(input_df)
        preds = model.predict(input_arr)
        return preds
    except Exception as e:
        raise CustomException(e, sys)
