# Use a small official Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list first so Docker can cache the install layer
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY . .

# Document the port the Flask app listens on
EXPOSE 5000

# Command that runs when the container starts
CMD ["python", "app.py"]
