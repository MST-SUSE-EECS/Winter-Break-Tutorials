# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /code

# Install FastAPI, Uvicorn, and SQLAlchemy using pip
RUN pip install --upgrade fastapi pymysql sqlalchemy
RUN pip install 'strawberry-graphql[fastapi]'
RUN pip install 'uvicorn[standard]'
RUN pip install cryptography

# Make port 80 available to the world outside this container
EXPOSE 8000
EXPOSE 80