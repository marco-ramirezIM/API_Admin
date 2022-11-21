from src.campaign import models,schemas
from src.campaign import exceptions
from sqlalchemy.orm import joinedload

def get_campaigns(db):
    campaigns=db.query(models.Campaign).all()
    if not campaigns:
        raise exceptions.server_error_exception
    return campaigns

def get_campaign(db,id):
    campaign = db.query(models.Campaign).\
    where(models.Campaign.id == id).first()
    if not campaign:
        raise exceptions.customer_error_exception("Campaign",id)
    return campaign
   

def get_campaigns_admin(db,admin_id):
    campaigns = db.query(models.Campaign).\
    where(models.Campaign.created_by==admin_id ).all()
    if not campaigns:
        raise exceptions.customer_error_exception("Admin",admin_id)
    return campaigns

def get_campaigns_client(db,client_id):
    campaigns = db.query(models.Campaign).\
    where(models.Campaign.client_id==client_id ).all()
    if not campaigns:
        raise exceptions.customer_error_exception("Client",admin_id)
    return campaigns