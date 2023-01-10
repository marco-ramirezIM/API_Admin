from datetime import datetime
from typing import List

from sqlalchemy import and_
import exceptions
from src.groupings.dependencies import (
    validate_duplicated_name,
    validate_company_user,
    validate_auditors,
)
from src.groupings.models import Grouping, UserGrouping, GroupingManagement
from src.groupings.schemas import GroupingBase, GroupingManagementBase
from src.groupings.exceptions import duplicated_value_exception
from src.companies.models import User
from azure import blob
import uuid

container_name = "imagenes"


def get_groupings(db) -> List[GroupingBase]:
    groupings = db.query(Grouping).where(Grouping.state == 1).all()
    return groupings or []


def get_grouping(db, id) -> GroupingBase:
    grouping = db.query(Grouping).where(Grouping.id == id).first()

    if not grouping:
        raise exceptions.entity_error_exception("agrupación", id)
    return grouping


def get_grouping_by_user(db, id) -> GroupingManagementBase:
    return db.query(GroupingManagement).where(GroupingManagement.company_id == id).all()


def update_grouping(id, grouping, data, db):
    grouping_check = get_grouping(db, id)
    if not grouping_check:
        raise exceptions.entity_error_exception("agrupación", id)

    if grouping_check.name != grouping.name and validate_duplicated_name(
        db, grouping.name
    ):
        raise duplicated_value_exception

    validate_auditors(db, grouping.users)
    if data is not None:
        blob.upload_blob(id + ".png", container_name, data)

    db.query(Grouping).filter(Grouping.id == id).update(
        {
            "name": grouping.name,
            "state": (1 if grouping.state else 0),
        }
    )
    db.commit()

    __delete_assigned_users(db, id)
    __created_user_grouping(db, grouping.users, id)
    return grouping_check


def create_grouping(grouping, data, db):

    if validate_duplicated_name(db, grouping.name):
        raise duplicated_value_exception

    validate_company_user(db, grouping.associated_company)

    validate_auditors(db, grouping.users)

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

    __created_associated_company(db, grouping.associated_company, new_grouping.id)
    __created_user_grouping(db, grouping.users, new_grouping.id)
    return new_grouping


def __created_associated_company(db, associated_company, grouping_id):
    db.add(
        UserGrouping(
            id=str(uuid.uuid4()),
            user_id=associated_company,
            grouping_id=grouping_id,
        )
    )


def __created_user_grouping(db, users, grouping_id):
    for user in users or []:
        result = UserGrouping(
            id=str(uuid.uuid4()),
            user_id=user,
            grouping_id=grouping_id,
        )
        db.add(result)
    db.commit()


def __delete_assigned_users(db, grouping_id):
    users = (
        db.query(UserGrouping.id)
        .join(User, User.id == UserGrouping.user_id)
        .filter(and_(UserGrouping.grouping_id == grouping_id, User.role_id == 3))
        .all()
    )

    users_ids = [r.id for r in users]

    db.query(UserGrouping).filter(UserGrouping.id.in_(users_ids)).delete()
    db.commit()
