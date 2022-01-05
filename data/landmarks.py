# import datetime
# from typing import List

import sqlalchemy as sa

# import sqlalchemy.orm as orm
from spookyMap.data.modelbase import SqlAlchemyBase

# from spookyMap.data.releases import Release

from dataclasses import dataclass


@dataclass
class Landmarks(SqlAlchemyBase):
    __tablename__ = "landmarks"
    id: int = sa.Column(sa.Integer(), primary_key=True)
    city: str = sa.Column(sa.Text())
    country: str = sa.Column(sa.Text())
    description: str = sa.Column(sa.Text())
    location: str = sa.Column(sa.Text())
    state: str = sa.Column(sa.Text())
    state_abbrev: str = sa.Column(sa.Text())
    latitude: float = sa.Column(sa.Float())
    longitude: float = sa.Column(sa.Float())
    city_latitude: float = sa.Column(sa.Float())
    city_longitude: float = sa.Column(sa.Float())

