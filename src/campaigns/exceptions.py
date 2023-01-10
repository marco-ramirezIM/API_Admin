from fastapi import HTTPException


def invalid_user_role_exception(name):
    return HTTPException(
        status_code=403, detail=f"El usuario {name} no tiene el rol requerido"
    )


def invalid_user_exception(id_list):
    return HTTPException(
        status_code=404,
        detail=f"la campaña no se puede crear porque los usuarios con el id {id_list} no existen",
    )


def invalid_user_exception_on_update(id_list):
    return HTTPException(
        status_code=404,
        detail=f"La campaña no se puede actualizar porque los usuarios con el id {id_list} no existen",
    )

def blob_does_not_exist_exception(name):
    return HTTPException(
        status_code=404,
        detail=f"La imagen con el nombre {name} no existe",
    )


duplicated_name_exception = HTTPException(
    403, "El nombre de la campaña que intenta crear ya existe"
)

grouping_not_found_exception = HTTPException(404, "Cliente no encontrado")
user_not_found_exception = HTTPException(404, "Usuarios no encontrados")
