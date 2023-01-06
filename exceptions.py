from fastapi import HTTPException, status


server_error_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="The request could not be completed.",
)


def entity_not_found_exception(type, id):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"El/la {type} con el id {id} no existe en la base de datos.",
    )

def entity_error_exception(error):
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Ocurrio un error al intentar {error}.",
    )

def duplicated_exception(type):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"El/la {type} ya se encuentra en uso.",
    )

token_b2c_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="The token was not found."
)
empty_fields_exception = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Some of the required fields are empty or are not valid.",
)
b2c_create_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Error al crear usuario",
)
b2c_update_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Error al actualizar el usuario",
)
b2c_disable_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Error al deshabilitar el usuario",
)

