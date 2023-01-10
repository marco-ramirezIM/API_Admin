from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
import src.groupings.service as service
from src.groupings.schemas import (
    GroupingBase,
    GroupingUpdate,
    GroupingManagementBase,
    GroupingCreate,
)
from config.db import Session
from typing import List, Union
from src.groupings.dependencies import (
    grouping_create_parameters,
    grouping_update_parameters,
)
import dependencies as dp
import exceptions

groupingRouter = APIRouter(tags=["Agrupaciones"])


@groupingRouter.get("/groupings", response_model=List[GroupingBase])
async def get_groupings(session: Session = Depends(dp.get_db)):
    try:
        return service.get_groupings(session)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener las agrupaciones")


@groupingRouter.get("/groupings/{grouping_id}", response_model=GroupingBase)
async def get_grouping(grouping_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_grouping(session, grouping_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener la agrupación")


@groupingRouter.get(
    "/groupings-by-company/{company_id}", response_model=List[GroupingManagementBase]
)
async def get_grouping_by_user(company_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_grouping_by_user(session, company_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception(
            "obtener las agrupaciones de un usuario"
        )


@groupingRouter.post("/groupings", response_model=GroupingBase)
async def create_grouping(
    file: Union[UploadFile, None] = None,
    grouping: GroupingCreate = Depends(grouping_create_parameters),
    session: Session = Depends(dp.get_db),
):
    try:
        if not file:
            raise exceptions.file_not_found_exception

        data = await file.read()
        dp.validate_file(file.content_type, data)
        return service.create_grouping(grouping, data, session)

    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("crear la agrupación")


@groupingRouter.put("/groupings/{grouping_id}", response_model=GroupingBase)
async def update_grouping(
    grouping_id: str,
    grouping: GroupingUpdate = Depends(grouping_update_parameters),
    file: Union[UploadFile, None] = None,
    session: Session = Depends(dp.get_db),
):
    try:

        data = None
        if file:
            data = await file.read()
            dp.validate_file(file.content_type, data)

        return service.update_grouping(grouping_id, grouping, data, session)

    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise exceptions.entity_error_exception("actualizar la agrupación")
