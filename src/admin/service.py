from src.admin import models,schemas
from src.admin import exceptions
from sqlalchemy.orm import joinedload
from src.admin.schemas import AdminBase,AdminUpdate

def get_administrators(db):
    administrators=db.query(models.Admin).\
    join(models.User).\
    where(models.User.state==1).\
    all()
    return administrators

def get_admin(db,id):
    admin = db.query(models.Admin).\
    where(models.Admin.id == id).first()
    if not admin:
        raise exceptions.customer_error_exception("Administrator",id)
    return admin

def update_admin(db,id,admin)-> AdminUpdate:
    admin_check=get_admin(db,id)
    db.query(models.Admin) \
        .filter(models.Admin.id == id) \
        .update({"phone":admin.phone, "photo":admin.photo, "company_name": admin.company_name, "minute_value": admin.minute_value}) 
    db.commit()
    return admin_check

def delete_admin(db,id):
    admin_check=get_admin(db,id)
    db.query(models.User) \
    .filter(models.User.id == admin_check.user_id) \
        .update({"state":0} ) 
    db.commit()

    return {f"the user of the admin with id {admin_check.id} was disabled"}