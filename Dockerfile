# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY app.py /app/
COPY requirements.txt /app/

# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8001

# Command to run the application
CMD ["python", "app.py"]

