from config.db import Session
from config.db import engine
import exceptions

max_file_size = 5000000
allowed_files = {"image/jpeg", "image/png", "image/gif", "image/tiff", "image/bmp"}


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


def validate_file_types(file_type):
    if not (file_type in allowed_files):
        raise exceptions.allowed_file_types_exception


def validate_max_file_size(data_file):
    if len(data_file) > max_file_size:
        raise exceptions.max_file_size_exception

def validate_file(file_type, data_file):
    validate_file_types(file_type)
    validate_max_file_size(data_file)