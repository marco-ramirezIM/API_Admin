from src.modules.schemas import ModuleUpdateOrCreate
from src.modules.models import Module
from src.modules.dependencies import (
    validate_category,
    validate_module_name,
    validate_campaign,
)
from datetime import datetime
import exceptions
from src.modules.exceptions import (
    category_not_found_exception,
    clusters_associated_to_modules_exception,
    module_not_found_exception,
    module_name_repeated_exception,
)
import uuid


def get_all_modules_by_campaign(campaign_id, db):
    validate_campaign(db, campaign_id)
    return db.query(Module).where(Module.campaign_id == campaign_id).all()


def get_module_by_id(db: str, id: str):
    module = db.query(Module).where(Module.id == id).first()
    if not module:
        raise exceptions.entity_not_found_exception("Compañia", id)
    return module


def update_module_by_id(db, id: str, data_module: ModuleUpdateOrCreate):

    if validate_category(db, data_module.category_id):
        raise category_not_found_exception

    validate_campaign(db, data_module.campaign_id)

    module_to_update = db.query(Module).where(Module.id == id).first()

    if module_to_update is None:
        raise module_not_found_exception

    if data_module.module != module_to_update.module and validate_module_name(
        db, data_module.module
    ):
        raise module_name_repeated_exception

    db.query(Module).filter(Module.id == id).update(
        {
            "campaign_id": data_module.campaign_id,
            "category_id": data_module.category_id,
            "module": data_module.module,
        }
    )
    db.commit()
    return {"id": id, **dict(data_module)}


def create_module(db, data_module: ModuleUpdateOrCreate):

    if validate_category(db, data_module.category_id):
        raise category_not_found_exception

    if validate_module_name(db, data_module.module):
        raise module_name_repeated_exception

    validate_campaign(db, data_module.campaign_id)

    new_module = Module(
        id=str(uuid.uuid4()),
        campaign_id=data_module.campaign_id,
        category_id=data_module.category_id,
        module=data_module.module,
        created_at=datetime.now(),
    )
    db.add(new_module)
    db.commit()
    return new_module
