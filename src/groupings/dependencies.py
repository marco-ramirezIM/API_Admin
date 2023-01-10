from src.groupings.models import Grouping
from src.companies.models import User
from src.groupings.exceptions import (
    invalid_company_exception,
    not_found_company_exception,
    invalid_audit_user_role_exception,
)
import src.campaigns.exceptions as campaing_exceptions


def validate_duplicated_name(db, name):
    name = db.query(Grouping).where(Grouping.name == name).first()
    return name is not None


def validate_company_user(db, user_id):
    user = db.query(User).where(User.id == user_id).first()
    if user is None:
        raise not_found_company_exception

    if user.role_id != 2:
        raise invalid_company_exception


def validate_auditors(db, users):
    if users is not None:
        users_result = db.query(User).filter(User.id.in_(users)).all()
        if not users_result:
            raise campaing_exceptions.user_not_found_exception

        invalid_users = list(
            map(lambda x: x.first_name, filter(lambda x: x.role_id != 3, users_result))
        )
        if len(invalid_users) > 0:
            raise invalid_audit_user_role_exception(" , ".join(invalid_users))
