from config.db import conn
from src.superAdmin.models import SuperAdmin
from src.superAdmin.schemas import superAdminEntity,superAdminsEntity

class SuperAdminService():

    def get_super_admins(self):
        return superAdminsEntity(conn.Development.superadministradores.find())