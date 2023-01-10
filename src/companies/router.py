from fastapi import APIRouter, Depends, HTTPException
from src.companies import service
import exceptions
from src.companies.schemas import CompanyBase, CompanyCreate, CompanyUpdate, UserBase
from config.db import Session
from typing import List
import dependencies as dp

companyRouter = APIRouter(tags=["Compañias"])


@companyRouter.get("/companies", response_model=List[CompanyBase])
async def get_companies(session: Session = Depends(dp.get_db)):
    try:
        return service.get_companies(session)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener las compañias")


@companyRouter.get("/companies/{company_id}", response_model=CompanyBase)
async def get_company(company_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_company(session, company_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener la compañia")


@companyRouter.post("/companies", response_model=UserBase)
async def create_company(company: CompanyCreate, session: Session = Depends(dp.get_db)):
    try:
        return service.create_company(company, session)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("crear la compañia")


@companyRouter.put("/companies/{company_id}", response_model=UserBase)
async def update_company(
    company_id: str, company: CompanyUpdate, session: Session = Depends(dp.get_db)
):
    try:
        return service.update_company(session, company_id, company)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("actualizar la compañia")
