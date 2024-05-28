# Use a Node.js base image
FROM node:14-alpine as build

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy the rest of the application code
COPY . .

# Build the application
RUN yarn build

# Use a lightweight web server to serve the built files
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port the app runs on
EXPOSE 8085

# Start the web server
CMD ["nginx", "-g", "daemon off;"]

