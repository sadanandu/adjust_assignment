from typing import List, Optional

from pydantic import BaseModel
import datetime

class DatasetBase(BaseModel):
    id : int
    date : datetime.date
    channel : str
    country : str
    os : str
    impressions : int
    clicks : int
    installs : int
    spend : int
    revenue : int

class DatasetCreate(DatasetBase):
    pass


class Dataset(DatasetBase):
    id : int
    date : datetime.date
    channel : str
    country : str
    os : str
    impressions : int
    clicks : int
    installs : int
    spend : int
    revenue : int

    class Config:
        orm_mode = True
