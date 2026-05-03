#!/usr/bin/env python
import os
import sys

# Set up the path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Now run the data ingestion
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    try:
        print("Starting ingestion pipeline...")
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()
        print(f"Data ingestion complete: train={train_data}, test={test_data}")

        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
        print(f"Data transformation complete")

        modeltrainer = ModelTrainer()
        r2_score = modeltrainer.initiate_model_trainer(train_arr, test_arr)
        print(f"Ingestion completed. Model R2 score: {r2_score}")
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
