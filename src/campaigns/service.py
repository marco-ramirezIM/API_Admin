from src.campaigns.models import Campaign, CampaignAccess
from src.groupings.models import Grouping
from src.campaigns.schemas import UpdateCampaign
import src.campaigns.dependencies as campaing_dependencies
import src.campaigns.exceptions as campaing_exceptions
import exceptions
import uuid
from datetime import datetime
import exceptions
from azure import blob

container_name = "imagenes"


def get_campaigns(db):
    return db.query(Campaign).all()


def get_campaign(db, id):
    campaign = db.query(Campaign).where(Campaign.id == id).first()
    if not campaign:
        raise exceptions.entity_not_found_exception("Campaña", id)
    return campaign


def get_campaigns_grouping(db, grouping_id):

    grouping = db.query(Grouping).filter(Grouping.id == grouping_id).all()

    if not grouping:
        raise campaing_exceptions.grouping_not_found_exception

    campaigns = db.query(Campaign).filter(Campaign.grouping_id == grouping_id).all()

    return campaigns


def get_campaings_agent(db, agent_id):

    campaigns = (
        db.query(Campaign)
        .join(CampaignAccess)
        .where(CampaignAccess.user_id == agent_id)
        .all()
    )

    return campaigns


def create_campaign(campaign, data, db):
    return
    id = str(uuid.uuid4())
    url_photo = blob.upload_blob(id + ".png", container_name, data)
    new_campaing = Campaign(
        id=id,
        name=campaign.name,
        photo=url_photo,
        state=(1 if campaign.state else 0),
        country=campaign.country,
        is_conversation=(1 if campaign.is_conversation else 0),
        is_mac=(1 if campaign.is_mac else 0),
        grouping_id=campaign.grouping_id,
        created_at=datetime.now(),
    )

    campaing_dependencies.is_valid_uuid(campaign.grouping_id)

    grouping = db.query(Grouping).filter(Grouping.id == campaign.grouping_id).first()

    if not grouping:
        raise campaing_exceptions.grouping_not_found_exception

    if campaing_dependencies.validate_duplicated_create(db, new_campaing):
        raise campaing_exceptions.duplicated_name_exception

    check_users = [""]
    if campaign.users[0] != "":
        for check_id in campaign.users:
            check_users_uuid_format = campaing_dependencies.is_valid_uuid(check_id)

            if not check_users_uuid_format:
                raise exceptions.entity_invalid_uuid_exception(check_id)

        check_users = campaing_dependencies.validate_users(db, campaign.users)

    users_not_inserted = []

    # diff = set(campaign.users_list) ^ set(check_users)

    for elem in campaign.users:
        if elem not in check_users:
            users_not_inserted.append(elem)

    if len(campaign.users) != len(check_users):
        raise campaing_exceptions.invalid_user_exception(users_not_inserted)
    return
    db.add(new_campaing)
    db.commit()

    campaing_dependencies.add_users_to_campaing(db, check_users, new_campaing.id)

    campaing_check = get_campaign(db, new_campaing.id)

    return campaing_check


def edit_campaign(db, id, data, campaign):

    check_campaign_id = campaing_dependencies.is_valid_uuid(id)

    if not check_campaign_id:
        raise exceptions.entity_invalid_uuid_exception(id)

    print("Imagen", type(data))
    print("Campaña", campaign)
    # first we validate if the campaign to edit exist
    campaign_to_update = get_campaign(db, id)

    if campaign_to_update:
        cp_id = campaign_to_update.id
        cp_photo = campaign_to_update.photo

    new_campaing = UpdateCampaign(
        state=campaign.state,
        users=campaign.users,
        is_conversation=campaign.is_conversation,
        is_mac=campaign.is_mac,
    )

    new_state = 1 if new_campaing.state else 0
    new_is_conversation = 1 if new_campaing.is_conversation else 0
    new_is_mac = 1 if new_campaing.is_mac else 0

    check_users = [""]
    users_not_inserted = []

    if new_campaing.users[0] == "" and len(new_campaing.users) == 1:
        campaing_dependencies.delete_users_of_campaign_on_update(db, cp_id)
    else:
        check_users = campaing_dependencies.validate_users(db, new_campaing.users)
        campaing_dependencies.add_users_to_campaign_on_update(db, check_users, cp_id)

    for elem in campaign.users:
        if elem not in check_users:
            users_not_inserted.append(elem)

    if len(new_campaing.users) != len(check_users):
        raise campaing_exceptions.invalid_user_exception_on_update(users_not_inserted)

    if type(data) == bytes:
        blob.delete_blob(cp_id + ".png")
        url_photo = blob.upload_blob(id + ".png", container_name, data)
        db.query(Campaign).filter(Campaign.id == id).update(
            {
                "photo": url_photo,
                "state": new_state,
                "is_conversation": new_is_conversation,
                "is_mac": new_is_mac,
            }
        )

    db.query(Campaign).filter(Campaign.id == id).update(
        {
            "state": new_state,
            "is_conversation": new_is_conversation,
            "is_mac": new_is_mac,
        }
    )

    db.commit()
    updated_campaing = get_campaign(db, id)
    return updated_campaing
