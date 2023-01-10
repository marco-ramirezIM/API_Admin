
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from src.categories.schemas import CategoryBase, CategoryUpdateOrCreate
import exceptions
import src.categories.service as service
from config.db import Session
import dependencies as dp

categoryRouter = APIRouter(tags=["Categorias"])

@categoryRouter.get("/categories-by-campaign/{campaign_id}", status_code=status.HTTP_200_OK, response_model=List[CategoryBase])
async def get_groupings(campaign_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_all_categories_by_campaign(session, campaign_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener las categorias")

@categoryRouter.get(
    "/categories/{id}", status_code=status.HTTP_200_OK, response_model=CategoryBase
)
async def get_category_by_id(id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_category_by_id(session, id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener la categoria por el id")


@categoryRouter.put(
    "/categories/{id}", status_code=status.HTTP_200_OK, response_model=CategoryBase
)
async def update_category_by_id(
    category: CategoryUpdateOrCreate, id: str, session: Session = Depends(dp.get_db)
):
    try:
        return service.update_category_by_id(session, id, category)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise exceptions.entity_error_exception("actualizar la categoria")


@categoryRouter.post(
    "/categories", status_code=status.HTTP_201_CREATED, response_model=CategoryBase
)
async def create_category(
    category: CategoryUpdateOrCreate, session: Session = Depends(dp.get_db)
):
    try:
        return service.create_category(session, category)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise exceptions.entity_error_exception("crear la categoria")