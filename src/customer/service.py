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
    customer_check=get_customer(db,id)
    if not customer_check:
        raise exceptions.entity_error_exception("Customer",id)
    db.query(models.Customer) \
        .filter(models.Customer.id == id) \
        .update({"name":customer.name, "photo":customer.photo}) 
    db.commit()
    return customer_check


def delete_customer(db,id):
    customer_check=get_customer(db,id)
    if not customer_check:
        raise exceptions.entity_error_exception("Customer",id)
    db.query(models.Client) \
    .filter(models.Client.id == customer_check.id) \
        .update({"state":0} ) 
    db.commit()

    return {f"the user of the customer with id {customer_check.id} was disabled"}

