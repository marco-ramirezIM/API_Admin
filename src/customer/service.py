
from src.customer import models,schemas
import exceptions
from sqlalchemy.orm import joinedload

def get_customers(db):
    customers=db.query(models.Client).all()
    if not customers:
        raise exceptions.server_error_exception
    return customers

def get_customer(db,id):
    customer = db.query(models.Client).\
    where(models.Client.id == id).first()
    if not customer:
        raise exceptions.entity_error_exception("Customer",id)
    return customer
   

def get_customers_admin(db,admin_id):
    customers = db.query(models.Client).\
    where(models.Client.created_by==admin_id ).all()
    if not customers:
        raise exceptions.entity_error_exception("Admin",admin_id)
    return customers

def get_customer_auditor():
    return {"auditor : cluster"}
    
def add_customer():
    return {"added:cluster"}

def update_customer():
    return {"updated:cluster"}

def delete_customer():
    return {"deleted:cluster"}

