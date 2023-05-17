FROM python:3.10-alpine3.17
WORKDIR /ecgvueweb
COPY ./requirements.txt /ecgvueweb/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /ecgvueweb/requirements.txt
COPY ./app /ecgvueweb/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


# FROM python:3.10-alpine3.17
# # Set the working directory inside the container
# WORKDIR /ecgvueweb
# # Copy the poetry.lock and pyproject.toml files
# COPY poetry.lock pyproject.toml /ecgvueweb/
# # Install Poetry
# RUN pip install poetry
# RUN pip install uvicorn
# RUN pip install gunicorn
# # Install project dependencies
# RUN poetry install --no-root
# # Copy the project code into the container
# COPY ./app /ecgvueweb/app
# # Start the app
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
