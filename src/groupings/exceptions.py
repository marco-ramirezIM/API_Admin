from fastapi import HTTPException

duplicated_value_exception = HTTPException(
    403,
    "Estas intentando guardar una agrupación que ya se encuentra registrado en la base de datos, por favor revisa los datos del formulario nuevamente",
)
