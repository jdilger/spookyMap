from sqlalchemy import text
from sqlalchemy.sql import expression
from sqlalchemy.sql.functions import func

import spookyMap.data.db_session as db_session
from spookyMap.data.landmarks import Landmarks


def get_landmarks_from_bounds(lngW, latS, lngE, latN):
    session = db_session.create_session()
    limit = 2000

    try:
        # # https://gis.stackexchange.com/questions/267087/how-do-i-get-all-geometries-within-area-using-google-maps-api-info
        # # do I need the create index? might be more preformat without since creating it each time map is paned
        # setup_sql = "CREATE INDEX ON landmarks USING GIST (ST_Transform(myGeom, 4326)); VACUUM ANALYZE myTable;"
        # # todo: check coords are right for expression ST_MakeEnvelope(xmin,ymin,xmax,ymax)
        sql = f"SELECT * FROM landmarks WHERE ST_Intersects(geom, ST_MakeEnvelope({lngW},{latS},{lngE},{latN}, 4326)) LIMIT {limit};"
        # # https://docs.sqlalchemy.org/en/14/orm/queryguide.html
        # # todo: figure out how to use text to select from landmarks
        landmarks = session.query(Landmarks).from_statement(text(sql)).all()

    finally:
        session.close()

    return landmarks


def get_random_from_db():
    session = db_session.create_session()
    try:
        random_landmark = (
            session.query(Landmarks).order_by(expression.func.random()).limit(1).first()
        )
    finally:
        session.close()
    return random_landmark
