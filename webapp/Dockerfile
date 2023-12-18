# Use an official Node.js runtime as the base image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and yarn.lock into the container
COPY package.json yarn.lock ./

# Install the application dependencies
RUN yarn install --frozen-lockfile

# Copy the rest of the application code into the container
COPY . .

# Expose port 3000 for the application
EXPOSE 3000

# Start the application when the container starts
CMD ["yarn", "start"]
