# import datetime
# from typing import List

import sqlalchemy as sa
# import sqlalchemy.orm as orm
from spookyMap.data.modelbase import SqlAlchemyBase
# from spookyMap.data.releases import Release

class Landmarks(SqlAlchemyBase):
    __tablename__ = 'landmarks'
    id = sa.Column(sa.Integer(), primary_key=True)
    city = sa.Column(sa.Text())
    country = sa.Column(sa.Text())
    description = sa.Column(sa.Text())
    location = sa.Column(sa.Text())
    state = sa.Column(sa.Text())
    state_abbrev = sa.Column(sa.Text())
    latitude = sa.Column(sa.Float())
    longitude = sa.Column(sa.Float())
    city_latitude = sa.Column(sa.Float())
    city_longitude = sa.Column(sa.Float())

