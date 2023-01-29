from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
import sys,os
from housing.logger import logging

class DataIngestion:
    def __init__(self,data_ingestion:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion started : {'='*20}")
            self.data_ingestion=data_ingestion
            
        
        except Exception as e:
          raise HousingException(sys,e) from e