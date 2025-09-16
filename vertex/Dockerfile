# Use the official Python image as the base
FROM --platform=linux/amd64 python:3.13.2

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Command to run your script when the container starts
CMD ["sh", "./run.sh", "8"]
