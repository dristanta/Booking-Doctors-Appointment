import re
from pydantic import BaseModel, Field, filed_validator

class DataTimeModel(BaseModel):
    data:str = Filed(description ='properly formated data')