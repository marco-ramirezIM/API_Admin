from src.modules.models import Module
from src.categories.models import Category
from src.campaigns.service import get_campaign


def validate_module_name(db, module: str):
    return (db.query(Module).where(Module.module == module).first()) is not None


def validate_category(db, id: str):
    return (db.query(Category).where(Category.id == id).first()) is None


def validate_campaign(db, id: str):
    get_campaign(db, id)
