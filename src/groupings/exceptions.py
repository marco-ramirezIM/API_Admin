from fastapi import HTTPException

def invalid_audit_user_role_exception(users):
    return HTTPException(
        status_code=403, detail=f"Los usuarios ({users}) no tienen el rol requerido"
    )


duplicated_value_exception = HTTPException(
    403,
    "Estas intentando guardar una agrupación que ya se encuentra registrado en la base de datos, por favor revisa los datos del formulario nuevamente",
)

invalid_company_exception = HTTPException(
    403,
    "Estas intentando guardar una agrupación asociada a una compañia invalida",
)


not_found_company_exception = HTTPException(
    403,
    "Estas intentando guardar una agrupación asociada a una compañia no existente",
)
