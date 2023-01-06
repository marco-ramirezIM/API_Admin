from fastapi import HTTPException


duplicated_value_exception = HTTPException(
    403,
    "Estas intentando guardar un dato que ya se encuentra registrado en la base de datos, por favor revisa los datos del formulario nuevamente",
)

password_exception = HTTPException(
    403, "The password must have at least one special character and one capital letter."
)
