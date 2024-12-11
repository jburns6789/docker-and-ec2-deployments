# Use the official Python image from the Docker Hub
FROM python:3.11-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

# Copy the application code
COPY . .

# Command to run the app
CMD ["python", "app.py"]
