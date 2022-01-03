import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from spookyMap.data.modelbase import SqlAlchemyBase


__factory = None


def global_init(db_conn_str: str):
    global __factory

    if __factory:
        return

    if not db_conn_str or not db_conn_str.strip():
        raise Exception("You must specify a db file.")

    conn_str = db_conn_str.strip()
    print("Connecting to DB with {}".format(conn_str))

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import spookyMap.data.__all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory

    session: Session = __factory()

    session.expire_on_commit = False

    return session