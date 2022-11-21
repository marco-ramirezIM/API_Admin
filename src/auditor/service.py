from config.db import conn
from src.auditor.models import User
from src.auditor.schemas import userEntity,usersEntity

class AuditorService():

    def get_auditors(self):
        return usersEntity(conn.Development.users.find())