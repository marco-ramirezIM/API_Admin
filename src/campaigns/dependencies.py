from src.campaigns.models import Campaign, CampaignAccess
import src.campaigns.exceptions as campaing_exceptions
from src.companies.models import User
import exceptions
import uuid


def validate_duplicated_create(db, campaing):
    campaing_name = db.query(Campaign).where(Campaign.name == campaing.name).first()
    return campaing_name

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def validate_users(db, users: list):
    #try:
    id_list = []
    users_result = db.query(User).filter(User.id.in_(users)).all()
    if not users_result:
        raise campaing_exceptions.user_not_found_exception

    for user in users_result:
        if user.role_id != 4:
            raise campaing_exceptions.invalid_user_role_exception(user.first_name)
        id_list.append(user.id)

    return id_list
    ''' except Exception:
        raise exceptions.entity_error_exception("encontrar el usuario") '''


def add_users_to_campaing(db, users_id: list, campaign_id: str):
    """If there are one or more users in the field campaign.users_list, we loop through every single user id and then insert them in the table campaigns_access"""
    try:
        __added_campaign_access_record(users=users_id, campaign_id=campaign_id, db=db)
    except Exception:
        raise exceptions.entity_error_exception("agregar las usuarios a la campaña")


def delete_users_of_campaign_on_update(db, campaign_id: str):

    print("Dependencies",campaign_id)

    db.query(CampaignAccess).filter(CampaignAccess.campaign_id == campaign_id).delete()
    db.commit()


def add_users_to_campaign_on_update(db, users: list, campaign_id: str):

    db.query(CampaignAccess).filter(CampaignAccess.campaign_id == campaign_id).delete()
    db.commit()

    __added_campaign_access_record(users=users, campaign_id=campaign_id, db=db)


def __added_campaign_access_record(users: list, campaign_id, db):
    for user in users:
        result = CampaignAccess(
            id=str(uuid.uuid4()),
            user_id=user,
            campaign_id=campaign_id,
        )
        db.add(result)
    db.commit()