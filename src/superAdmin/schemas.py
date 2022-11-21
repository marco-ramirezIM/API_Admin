def superAdminEntity(item)->dict:
    return{
    #"id":item["_id"],
    "names":item["nombres"],
    "email":item["correo"],
    "role":item["role"],
    "state":item["state"],
    "createdAt":item["createdAt"]
    }

def superAdminsEntity (entity) -> list:
    return [superAdminEntity(item) for item in entity]