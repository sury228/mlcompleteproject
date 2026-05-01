import os
import sys

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

if __name__ == '__main__':
    try:
        logging.info('Starting training pipeline')

        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()

        transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(train_path, test_path)

        trainer = ModelTrainer()
        model_path, r2 = trainer.initiate_model_trainer(train_arr, test_arr)

        logging.info(f'Preprocessor saved to: {preprocessor_path}')
        logging.info(f'Model saved to: {model_path}')
        logging.info(f'Model R2 score: {r2:.4f}')
    except Exception as e:
        raise CustomException(e, sys)
