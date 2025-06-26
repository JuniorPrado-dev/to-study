# Topcs
 - PHP# Use an official MongoDB image as a parent image
FROM mongo:latest

# Create a directory to store MongoDB data
RUN mkdir -p /data/db

# Set permissions for the directory
RUN chmod -R 777 /data/db# Use an official MongoDB image as a parent image
FROM mongo:latest

# Create a directory to store MongoDB data
RUN mkdir -p /data/db

# Set permissions for the directory
RUN chmod -R 777 /data/db

# Expose the default MongoDB port
EXPOSE 27017

# Start MongoDB when the container launches
CMD ["mongod"]


# Expose the default MongoDB port
EXPOSE 27017

# Start MongoDB when the container launches
CMD ["mongod"]

# Run Container
docker build -t mongo-image .
docker run -d --name mongo-container -p 27017:27017 my-mongo

# Using Compose
docker compose up -d

# URL para o mongo compass:
mongodb://<usuario>:<senha>@<host>:<porta>/<banco>
