from src.groupings.models import Grouping


def validate_duplicated_name(db, name):
    name = db.query(Grouping).where(Grouping.name == name).first()

    return name is not None
