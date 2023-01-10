from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
import src.groupings.service as service
from src.groupings.schemas import GroupingBase, GroupingCreate
from config.db import Session
from typing import List, Union
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


@groupingRouter.post("/groupings")
async def create_grouping(
    name: str = Form(...),
    state: bool = Form(...),
    users: Union[List[str], None] = None,
    file: Union[UploadFile, None] = None,
    session: Session = Depends(dp.get_db),
):
    try:

        if not file:
            raise exceptions.file_not_found_exception

        data = await file.read()
        dp.validate_file(file.content_type, data)

        grouping = GroupingCreate(name=name, state=state, users=users)
        return service.create_grouping(grouping, data, session)

    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("Crear la agrupación")