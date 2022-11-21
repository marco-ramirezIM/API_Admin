from src.admin import models,schemas
from sqlalchemy.orm import joinedload

def get_administrators(db):
    administrators=db.query(models.Admin).all()
    return administrators