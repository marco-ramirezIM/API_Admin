from src.companies.models import Company
from src.companies.exceptions import password_exception
import exceptions
import re


def get_company(db, id):
    company = db.query(Company).where(Company.id == id).first()
    if not company:
        raise exceptions.entity_error_exception("Compañia", id)
    return company


def validate_duplicated_create(db, company):
    phone = db.query(Company).where(Company.phone == company.phone).first()

    identification = (
        db.query(Company)
        .where(Company.identification == company.identification)
        .first()
    )

    company_name = (
        db.query(Company).where(Company.company_name == company.company_name).first()
    )

    email = db.query(Company).where(Company.email == company.email).first()

    return phone or identification or company_name or email


def validate_update_phone(db, company, id):
    check_phone = db.query(Company).where(Company.phone == company.phone).first()
    company_check = get_company(db, id)
    if company.phone != company_check.phone and check_phone:
        return True


def validate_update_company_name(db, company, id):
    check_company_name = (
        db.query(Company).where(Company.company_name == company.company_name).first()
    )
    company_check = get_company(db, id)
    if company.company_name != company_check.company_name and check_company_name:
        return True


def validate_update_email(db, company, id):
    check_email = db.query(Company).where(Company.email == company.email).first()
    company_check = get_company(db, id)
    if company.email != company_check.email and check_email:
        return True


def validate_update_identification(db, company, id):
    check_identification = (
        db.query(Company)
        .where(Company.identification == company.identification)
        .first()
    )
    company_check = get_company(db, id)
    if company.identification != company_check.identification and check_identification:
        return True


def verify_password(password):
    password_pattern = (
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    )
    if not re.search(password_pattern, password):
        raise password_exception
