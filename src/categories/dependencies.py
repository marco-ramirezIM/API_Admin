from src.campaigns.service import get_campaign
from src.categories.models import Category

def validate_campaign(db, id: str):
    get_campaign(db, id)


def validate_category_name(db, category: str):
    return (db.query(Category).where(Category.category == category).first()) is not None