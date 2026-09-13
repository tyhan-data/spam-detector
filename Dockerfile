# Use python 3.13 as base image
FROM python:3.13-slim

# Set the working folder inside the container
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Port Address
EXPOSE 8000

# Start streamlit server
CMD [ "uvicorn", "app.main:app",  "--host", "0.0.0.0", "--port", "8000" ]