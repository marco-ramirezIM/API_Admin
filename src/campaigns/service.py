from src.campaigns.models import Campaign, CampaignAccess
from src.groupings.models import Grouping
from src.campaigns.schemas import UpdateCampaign
import src.campaigns.dependencies as campaing_dependencies
import src.campaigns.exceptions as campaing_exceptions
import exceptions
import uuid
from datetime import datetime
import exceptions


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


def create_campaign(campaign, db):
    new_campaing = Campaign(
        id=str(uuid.uuid4()),
        name=campaign.name,
        photo=campaign.photo,
        state=campaign.state,
        country=campaign.country,
        is_conversation=campaign.is_conversation,
        is_mac=campaign.is_mac,
        grouping_id=campaign.grouping_id,
        created_at=datetime.now(),
    )

    grouping = db.query(Grouping).filter(Grouping.id == campaign.grouping_id).first()

    if not grouping:
        raise campaing_exceptions.grouping_not_found_exception

    if campaing_dependencies.validate_duplicated_create(db, new_campaing):
        raise campaing_exceptions.duplicated_name_exception

    check_users = []
    if len(campaign.users_list) > 0:
        check_users = campaing_dependencies.validate_users(db, campaign.users_list)

    users_not_inserted = []

    # diff = set(campaign.users_list) ^ set(check_users)

    for elem in campaign.users_list:
        if elem not in check_users:
            users_not_inserted.append(elem)

    if len(campaign.users_list) != len(check_users):
        raise campaing_exceptions.invalid_user_exception(users_not_inserted)

    db.add(new_campaing)
    db.commit()

    campaing_dependencies.add_users_to_campaing(db, check_users, new_campaing.id)

    campaing_check = get_campaign(db, new_campaing.id)

    return campaing_check


def edit_campaign(db, id, campaign):
    # first we validate if the campaign to edit exist
    campaign_to_update = get_campaign(db, id)

    if campaign_to_update:
        campaign_id = campaign_to_update.id

    new_campaing = UpdateCampaign(
        photo=campaign.photo,
        state=campaign.state,
        users_list=campaign.users_list,
        is_conversation=campaign.is_conversation,
        is_mac=campaign.is_mac,
    )

    check_users = []
    users_not_inserted = []

    if len(new_campaing.users_list) == 0:
        campaing_dependencies.delete_users_of_campaign_on_update(db, campaign_id)
    else:
        check_users = campaing_dependencies.validate_users(db, new_campaing.users_list)
        campaing_dependencies.add_users_to_campaign_on_update(
            db, check_users, campaign_id
        )

    for elem in campaign.users_list:
        if elem not in check_users:
            users_not_inserted.append(elem)

    if len(new_campaing.users_list) != len(check_users):
        raise campaing_exceptions.invalid_user_exception_on_update(users_not_inserted)

    db.query(Campaign).filter(Campaign.id == id).update(
        {
            "photo": new_campaing.photo,
            "state": new_campaing.state,
            "is_conversation": new_campaing.is_conversation,
            "is_mac": new_campaing.is_mac,
        }
    )

    db.commit()
    updated_campaing = get_campaign(db, id)
    return updated_campaing
