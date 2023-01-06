from src.campaign.models import Campaign, CampaingAccess
from fastapi import HTTPException
import src.campaign.exceptions as campaing_exceptions
from src.admin.models import User
from sqlalchemy import and_
import random
import string


def validate_duplicated_create(db, campaing):
    campaing_name = db.query(Campaign).where(Campaign.name == campaing.name).first()
    return campaing_name


def validate_users(db, users: list):
    try:
        id_list = []
        users_result = db.query(User).filter(User.id.in_(users)).all()

        if not users_result:
            raise campaing_exceptions.user_not_found_exception

        for user in users_result:
            if user.role_id != 4:
                raise campaing_exceptions.invalid_user_role_exception(user.first_name)
            id_list.append(user.id)

        return id_list
    except HTTPException as e:
        raise e
    except Exception:
        raise campaing_exceptions.validate_user_exception


def add_users_to_campaing(db, users: list, campaign_id: str):
    """If there are one or more users in the field campaign.users_list, we loop through every single user id and then insert them in the table campaigns_access"""
    try:
        for user in users:
            result = CampaingAccess(
                id="".join(random.choices(string.ascii_letters + string.digits, k=24)),
                user_id=user,
                campaing_id=campaign_id,
            )
            db.add(result)
        db.commit()
    except HTTPException as e:
        raise e
    except Exception:
        raise campaing_exceptions.add_users_to_campaing_exception


def delete_users_of_campaign_on_update(db, campaign_id: str):

    db.query(CampaingAccess).filter(CampaingAccess.campaing_id == campaign_id).delete()
    db.commit()


def add_users_to_campaign_on_update(db, users: list, campaign_id: str):

    db.query(CampaingAccess).filter(CampaingAccess.campaing_id == campaign_id).delete()
    db.commit()

    for user in users:
        result = CampaingAccess(
            id="".join(random.choices(string.ascii_letters + string.digits, k=24)),
            user_id=user,
            campaing_id=campaign_id,
        )
        db.add(result)
    db.commit()
