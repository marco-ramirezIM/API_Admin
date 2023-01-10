from datetime import datetime
import random, string
from typing import List
import exceptions
from src.groupings.dependencies import validate_duplicated_name
from src.groupings.models import Grouping
from src.groupings.schemas import GroupingBase
from src.groupings.exceptions import duplicated_value_exception
from azure import blob
import uuid

container_name = "imagenes"

def get_groupings(db) -> List[GroupingBase]:
    groupings = db.query(Grouping).where(Grouping.state == 1).all()
    return groupings or []


def get_grouping(db, id) -> GroupingBase:
    grouping = db.query(Grouping).where(Grouping.id == id).first()

    if not grouping:
        raise exceptions.entity_error_exception("Grouping", id)
    return grouping


def update_grouping(db, id, grouping):
    grouping_check = get_grouping(db, id)

    if not grouping_check:
        raise exceptions.entity_error_exception("Grouping", id)

    if grouping_check.name != grouping.name and validate_duplicated_name(db, grouping):
        raise duplicated_value_exception

    db.query(Grouping).filter(Grouping.id == id).update(
        {
            "name": grouping.name,
            "photo": grouping.photo,
            "state": (1 if grouping.state else 0),
        }
    )
    db.commit()

    return grouping_check


def create_grouping(grouping, data, db):

    if validate_duplicated_name(db, grouping.name):
        raise duplicated_value_exception

    id = str(uuid.uuid4())
    url_photo = blob.upload_blob(id + ".png", container_name, data)
    new_grouping = Grouping(
        id=id,
        name=grouping.name,
        photo=url_photo,
        created_at=datetime.now(),
        state=(1 if grouping.state else 0),
    )

    db.add(new_grouping)
    db.commit()
    grouping_check = get_grouping(db, new_grouping.id)
    return grouping_check
