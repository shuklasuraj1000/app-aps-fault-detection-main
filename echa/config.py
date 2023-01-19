import pymongo
import json
import pandas as pd
from dataclasses import dataclass
import os
# Provide the mongodb localhost url to connect python to mongodb.


@dataclass
class EnvironmentVariable:
    db_file_path:str = os.getenv("db_file_path")
    web_link = os.getenv("web_link")
    driver_path = os.getenv("driver_path")
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
db_name ="ACF_ACR"
coll_name ="REACH"
