FROM python:3.9
COPY ./ /app-admin
RUN pip install --no-cache-dir --upgrade -r /app-admin/requirements.txt
COPY ./ /app-admin
WORKDIR /app-admin
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]