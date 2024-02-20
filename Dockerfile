FROM python:3.8-alpine

# Set working directory
WORKDIR /app

# Copy requirements.txt to the container at /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Specify the command to run on container start
CMD ["python3", "app.py"]