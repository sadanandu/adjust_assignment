from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date,Float
from sqlalchemy.orm import relationship

from .database import Base


class Dataset(Base):
    __tablename__ = "dataset"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    channel = Column(String, index=True)
    country = Column(String, index=True)
    os = Column(String, index=True)
    impressions = Column(Integer, index=True)
    clicks = Column(Integer, index=True)
    installs = Column(Integer, index=True)
    spend = Column(Float , index=True)
    revenue = Column(Float, index=True)
