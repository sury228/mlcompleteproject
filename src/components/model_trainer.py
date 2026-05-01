import os
import sys
import numpy as np
from dataclasses import dataclass
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array: np.ndarray, test_array: np.ndarray):
        try:
            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            r2 = r2_score(y_test, y_pred)

            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=model)
            return self.model_trainer_config.trained_model_file_path, r2
        except Exception as e:
            raise CustomException(e, sys)
