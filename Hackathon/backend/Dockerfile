# Use the official Python 3.10 base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy requirements.txt in the working directory in the container
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000