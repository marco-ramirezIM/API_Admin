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
            

def __validate_update_phone(db,admin,id):
        check_phone=db.query(models.Admin).\
            where(models.Admin.phone == admin.phone).first()
        admin_check=get_admin(db,id)
        if admin.phone!=admin_check.phone and check_phone:
            return True

def __validate_update_company_name(db,admin,id):
        check_company_name=db.query(models.Admin).\
            where(models.Admin.company_name == admin.company_name).first()
        admin_check=get_admin(db,id)
        if admin.company_name!=admin_check.company_name and check_company_name:
            return True


def get_administrators(db):
    administrators=db.query(models.Admin).all()
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
    if __validate_update_phone(db,admin,id):
        raise duplicated_value_exception
    if __validate_update_company_name(db,admin,id):
        raise duplicated_value_exception
    db.query(models.Admin) \
        .filter(models.Admin.id == id) \
        .update({"first_name":admin.first_name,"last_name":admin.last_name,
        "phone":admin.phone,"identification":admin.identification,
        "email":admin.email,"password":admin.password,
        "state":admin.state, "photo":admin.photo,
        "company_name": admin.company_name}) 
    db.commit()
    return admin_check

def delete_admin(db,id):
    admin_check=get_admin(db,id)
    if not admin_check:
        raise exceptions.entity_error_exception("Administrator",id)
    db.query(models.Admin) \
    .filter(models.Admin.id == admin_check.id) \
        .update({"state":0} ) 
    db.commit()

    return {f"the Admin of the admin with id {admin_check.id} was disabled"}

def create_admin(admin,db):
    new_admin=Admin(id=''.join(random.choices(string.ascii_letters + string.digits, k=24)),
    role_id=2 ,first_name=admin.first_name,last_name=admin.last_name,
    phone=admin.phone,identification=admin.identification,
    email=admin.email,password=admin.password,
    state=1, photo=admin.photo,
    company_name=admin.company_name,created_at=datetime.now(),
    )
    if  __validate_duplicated_create(db,new_admin):
        raise duplicated_value_exception
    db.add(new_admin)
    db.commit()
    admin_check=get_admin(db,new_admin.id)
    return admin_check



    