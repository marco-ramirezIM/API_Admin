from fastapi import APIRouter,Depends
from src.customer import service
from src.customer.schemas import Customer
from config.db import Session
from typing import List
from src.customer import dependencies as dp

customerRouter=APIRouter(tags=["Customer"])

@customerRouter.get('/customers',response_model=List[Customer])
async def get_customers(session:Session=Depends(dp.get_db)):
    return service.get_customers(session)

@customerRouter.get('/customers/{customer_id}',response_model=Customer)
async def get_customer(customer_id:str,session:Session=Depends(dp.get_db)):
    return service.get_customer(session,customer_id)

@customerRouter.get('/customers/admin/{admin_id}',response_model=List[Customer])
async def get_customers_admin(admin_id:str,session:Session=Depends(dp.get_db)):
    return service.get_customers_admin(session,admin_id)

