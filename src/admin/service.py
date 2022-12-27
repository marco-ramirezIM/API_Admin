import random, string
from src.admin import models,schemas
import exceptions
from sqlalchemy.orm import joinedload
from src.admin.schemas import AdminBase,AdminUpdate
from src.admin.models import Admin
from src.admin.exceptions import duplicated_value_exception
from datetime import datetime


def __validate_duplicated_create(db,admin):
        phone=db.query(models.Admin).\
            where(models.Admin.phone == admin.phone).first()

        identification=db.query(models.Admin).\
            where(models.Admin.identification == admin.identification).first()

        company_name=db.query(models.Admin).\
            where(models.Admin.company_name == admin.company_name).first()

        return  (phone or identification or company_name)
            

def __validate_duplicated_update(db,admin):
        phone=db.query(models.Admin).\
            where(models.Admin.phone == admin.phone).first()

        company_name=db.query(models.Admin).\
            where(models.Admin.company_name == admin.company_name).first()

        return (phone or company_name)
          
        
def get_administrators(db):
    administrators=db.query(models.Admin).\
    join(models.User).\
    where(models.User.state==1).\
    all()
    if not administrators:
        raise exceptions.server_error_exception
    return administrators

def get_admin(db,id):
    admin = db.query(models.Admin).\
    where(models.Admin.id == id).first()
    if not admin:
        raise exceptions.entity_error_exception("Administrator",id)
    return admin

def update_admin(db,id,admin)-> AdminUpdate:
    admin_check=get_admin(db,id)
    if not admin:
        raise exceptions.entity_error_exception("Administrator",id)
    if __validate_duplicated_update(db,admin):
        raise duplicated_value_exception
    db.query(models.Admin) \
        .filter(models.Admin.id == id) \
        .update({"phone":admin.phone, "photo":admin.photo, "company_name": admin.company_name, "minute_value": admin.minute_value}) 
    db.commit()
    return admin_check

def delete_admin(db,id):
    admin_check=get_admin(db,id)
    if not admin:
        raise exceptions.entity_error_exception("Administrator",id)
    db.query(models.User) \
    .filter(models.User.id == admin_check.user_id) \
        .update({"state":0} ) 
    db.commit()

    return {f"the user of the admin with id {admin_check.id} was disabled"}

def create_admin(user,admin,db):
    new_admin=Admin(id=''.join(random.choices(string.ascii_letters + string.digits, k=24))
    ,phone=admin.phone,
    photo=admin.photo,company_name=admin.company_name,
    identification=admin.identification,created_at=datetime.now(),
    minute_value=admin.minute_value,user_id=admin.user_id)
    if  __validate_duplicated_create(db,new_admin):
        raise duplicated_value_exception
    db.add(new_admin)
    db.commit()
    admin_check=get_admin(db,new_admin.id)
    return admin_check



    