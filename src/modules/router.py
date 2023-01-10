from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from src.modules.schemas import ModuleBase, ModuleUpdateOrCreate, ModuleList
from config.db import Session
import dependencies as dp
import src.modules.service as service
import exceptions

modulesRouter = APIRouter(tags=["Modules"])


@modulesRouter.get(
    "/modules-by-campaing/{campaign_id}",
    status_code=status.HTTP_200_OK,
    response_model=List[ModuleList],
)
async def get_all_modules(campaign_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_all_modules_by_campaign(campaign_id, session)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception(
            "obtener el modulo por el id de la campaña"
        )


@modulesRouter.get(
    "/modules/{id}", status_code=status.HTTP_200_OK, response_model=ModuleList
)
async def get_module_by_id(id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_module_by_id(session, id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener el modulo por el id")


@modulesRouter.put(
    "/modules/{id}", status_code=status.HTTP_200_OK, response_model=ModuleBase
)
async def update_module_by_id(
    data_module: ModuleUpdateOrCreate, id: str, session: Session = Depends(dp.get_db)
):
    try:
        return service.update_module_by_id(session, id, data_module)
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise exceptions.entity_error_exception("actualizar el modulo")


@modulesRouter.post(
    "/modules", status_code=status.HTTP_201_CREATED, response_model=ModuleBase
)
async def create_module(
    data_module: ModuleUpdateOrCreate, session: Session = Depends(dp.get_db)
):
    try:
        return service.create_module(session, data_module)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("crear el modulo")

