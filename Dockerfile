# Use python 3.13 as base image
FROM python:3.13-slim

# Set the working folder inside the container
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project
COPY . .

# Port Address
EXPOSE 8501

# Start streamlit server
CMD [ "streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501" ]