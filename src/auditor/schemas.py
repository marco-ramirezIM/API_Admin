def userEntity(item)->dict:
    return{
    #"id":item["_id"],
    "names":item["nombres"],
    "email":item["correo"],
    "role":item["role"],
    "state":item["state"],
    "clusters":str(item["clusters"]),
    "createdBy":str(item["createdBy"]),
    "createdAt":item["createdAt"]
    }

def usersEntity (entity) -> list:
    return [userEntity(item) for item in entity]