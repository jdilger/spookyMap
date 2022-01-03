from typing import List, Optional
import sqlalchemy.orm
from sqlalchemy.orm import Session

import spookyMap.data.db_session as db_session
from spookyMap.data.landmarks import Landmarks


def get_landmarks_from_bounds(lngW, latS, lngE, latN):
    session = db_session.create_session()
    
    try:
        # https://gis.stackexchange.com/questions/267087/how-do-i-get-all-geometries-within-area-using-google-maps-api-info
        # do I need the create index? might be more preformat without since creating it each time map is paned
        setup_sql = 'CREATE INDEX ON landmarks USING GIST (ST_Transform(myGeom, 4326)); VACUUM ANALYZE myTable;'
        # todo: check coords are right for expression ST_MakeEnvelope(xmin,ymin,xmax,ymax)
        sql = f'SELECT * FROM landmarks WHERE ST_MakeEnvelope({lngW},{latS},{lngE},{latN}) && ST_Transform(myTable.geom,4326);'
        # https://docs.sqlalchemy.org/en/14/orm/queryguide.html
        # todo: figure out how to use text to select from landmarks
        landmarks = session.query(Landmarks). \
            options(sqlalchemy.orm.joinedload(Release.package)). \
            order_by(Release.created_date.desc()). \
            limit(limit). \
            all()

    finally:
        session.close()

    return releases