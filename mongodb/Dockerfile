# Use an official MongoDB image as a parent image
FROM mongo:latest

# Create a directory to store MongoDB data
RUN mkdir -p /data/db

# Set permissions for the directory
RUN chmod -R 777 /data/db

# Expose the default MongoDB port
EXPOSE 27017

# Start MongoDB when the container launches
CMD ["mongod"]
