# Base image
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Copy the .env file
COPY .env /app/.env

COPY create_superuser.py /app/create_superuser.py

# Run migrations and start the application
CMD ["sh", "-c", "python manage.py migrate && python /app/create_superuser.py && python manage.py runserver 0.0.0.0:8000"]

