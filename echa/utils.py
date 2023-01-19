import pandas as pd
from pandas import DataFrame
import numpy as np
from echa.exception import ECHAException
from echa.logger import logging
from echa.config import mongo_client
import sys


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    will detect db_file_path as enviroment variable
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        #logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        #logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            #logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        #logging.info(f"Row and columns in df: {df.shape}")
        
        df.replace("", np.NaN, inplace=True)
        
        return df
    
    except Exception as e:
        raise ECHAException(e, sys)
    
