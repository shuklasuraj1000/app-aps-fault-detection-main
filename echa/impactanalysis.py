import pandas as pd
import numpy as np
from echa.config import db_name, coll_name
from echa import utils
from echa.logger import logging

def impact_analysis(m):
  """
  This function will check if given part number is REACH Impacted or not.
  This function check base number > material code > finish in sequence.
  Please enter part number as Input
  """
  # Load ACR & ACF database from db.csv file as DataFrame
  logging.info(">>>>>>>>> SEARCH STARTED FOR PART : {} <<<<<<<<<<<".format(m))
  df:pd.DataFrame = utils.get_collection_as_dataframe(database_name = db_name, collection_name=coll_name)
  #logging.info(f"loaded ACF_ACR db for impact analysis, REACHdb_shape: {df.shape}")
  #print(df)
  
  for i in range(len(df['PART_NUMBER'])):
    # Checking if STD and Base part number matches >>>>>
    if m.startswith(df.iloc[i,0]) == True or m.startswith(df.iloc[i,1]) == True:
      #logging.info("STD found")      
      # Checking if material code is given or not
      if pd.isna(df.iloc[i,2])== True:                 # if Level-2
        #logging.info("No material code")   # >>>>>>>>>>>>>>>>>
        if pd.isna(df.iloc[i,3]) ==True:               # if Level-3
          logging.info("Part status : {}".format(df.iloc[i,4]))
          return (m, df.iloc[i,4], df.iloc[i,5], df.iloc[i,6], df.iloc[i,8])
        else:
          if m.find(str(df.iloc[i,3])) >= len(df.iloc[i,0]) or m.find(str(df.iloc[i,3])) >= len(df.iloc[i,1]):  # else Level-3
            logging.info("Part status : {}".format(df.iloc[i,4]))
            return (m, df.iloc[i,4], df.iloc[i,5], df.iloc[i,6], df.iloc[i,8])
          else:
            logging.info("Finish code not found")

      else:
        if m.find(str(df.iloc[i,2]))>= len(df.iloc[i,0]) or m.find(str(df.iloc[i,2]))>= len(df.iloc[i,1]): # else Level-2
         #logging.info("Material code found")  # >>>>>>>>>>>>>>>
         if pd.isna(df.iloc[i,3]) ==True:              # if Level-3
          logging.info("Part status : {}".format(df.iloc[i,4]))
          return (m, df.iloc[i,4], df.iloc[i,5], df.iloc[i,6], df.iloc[i,8])
         else:
           if m.find(str(df.iloc[i,3])) >= m.find(str(df.iloc[i,2])):  # else Level-3
             #logging.info("Finish code found")
             logging.info("Part status : {}".format(df.iloc[i,4]))
             return (m, df.iloc[i,4], df.iloc[i,5], df.iloc[i,6], df.iloc[i,8])
           else:
             logging.info ("Finish code not found")

    else:
      pass
  
  
