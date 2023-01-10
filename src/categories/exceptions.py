from fastapi import HTTPException

category_name_repeated_exception = HTTPException(403, "El nombre de la categoria que está intentando crear ya existe")
category_not_found_exception = HTTPException(404, detail="Categoria no encontrada")