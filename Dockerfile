FROM python:3.8-slim-buster

WORKDIR /app

# Install PostgreSQL development libraries
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
