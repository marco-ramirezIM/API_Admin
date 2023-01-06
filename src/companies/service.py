import exceptions
from src.companies.schemas import CompanyUpdate
from src.companies.models import Company
from src.companies.exceptions import duplicated_value_exception
import src.companies.dependencies as company_dep
from datetime import datetime
from config import b2c


def get_companies(db):
    companies = db.query(Company).all()
    if not companies:
        raise exceptions.server_error_exception
    return companies


def get_company(db, id):
    company = db.query(Company).where(Company.id == id).first()
    if not company:
        raise exceptions.entity_not_found_exception("Compañia", id)
    return company


def update_company(db, id, company) -> CompanyUpdate:
    company_check = get_company(db, id)
    company_dep.verify_password(company.password)
    if not company:
        raise exceptions.entity_not_found_exception("Compañia", id)
    if company_dep.validate_update_phone(db, company, id):
        raise exceptions.duplicated_exception("Telefono")
    if company_dep.validate_update_company_name(db, company, id):
        raise exceptions.duplicated_exception("Nombre de la compañia")
    if company_dep.validate_update_email(db, company, id):
        raise exceptions.duplicated_exception("Email")
    if company_dep.validate_update_identification(db, company, id):
         raise exceptions.duplicated_exception("Documento de identificacion")
    b2c.graph_update(id, company)
    db.query(Company).filter(Company.id == id).update(
        {
            "first_name": company.first_name,
            "last_name": company.last_name,
            "phone": company.phone,
            "identification": company.identification,
            "email": company.email,
            "password": company.password,
            "state": company.state,
            "photo": company.photo,
            "company_name": company.company_name,
        }
    )
    db.commit()
    return company_check


def create_company(company, db):
    company_dep.verify_password(company.password)
    if company_dep.validate_duplicated_create(db, company):
        raise duplicated_value_exception
    new_id = b2c.graph_create(company)
    if not new_id:
        raise exceptions.empty_fields_exception
    new_company = Company(
        id=new_id,
        role_id=2,
        first_name=company.first_name,
        last_name=company.last_name,
        phone=company.phone,
        identification=company.identification,
        email=company.email,
        password=company.password,
        state=1,
        photo=company.photo,
        company_name=company.company_name,
        created_at=datetime.now(),
    )
    db.add(new_company)
    db.commit()
    company_check = get_company(db, new_company.id)
    return company_check
