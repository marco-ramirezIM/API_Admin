from src.categories.models import Category
from src.categories.dependencies import validate_campaign
from src.categories.schemas import CategoryUpdateOrCreate
from src.categories.dependencies import validate_category_name
from src.categories.exceptions import category_name_repeated_exception, category_not_found_exception
import exceptions
from datetime import datetime
import uuid

def get_all_categories_by_campaign(db, campaign_id):
    validate_campaign(db, campaign_id)
    return db.query(Category).where(Category.campaign_id == campaign_id).all()

def get_category_by_id(db: str, id: str):
    category = db.query(Category).where(Category.id == id).first()
    if not category:
        raise exceptions.entity_not_found_exception("categoria", id)
    return category

def create_category(db, category: CategoryUpdateOrCreate):

    if validate_category_name(db, category.category):
        raise category_name_repeated_exception

    validate_campaign(db, category.campaign_id)

    new_category = Category(
        id=str(uuid.uuid4()),
        campaign_id=category.campaign_id,
        category=category.category,
        created_at=datetime.now(),
    )
    db.add(new_category)
    db.commit()
    return new_category

def update_category_by_id(db, id: str, category: CategoryUpdateOrCreate):

    validate_campaign(db, category.campaign_id)

    category_to_update = db.query(Category).where(Category.id == id).first()

    if category_to_update is None:
        raise category_not_found_exception

    if category.category != category.category and validate_category_name(
        db, category.category
    ):
        raise category_name_repeated_exception

    db.query(Category).filter(Category.id == id).update(
        {
            "campaign_id": category.campaign_id,
            "category": category.category,
        }
    )
    db.commit()
    return {"id": id, **dict(category)}

