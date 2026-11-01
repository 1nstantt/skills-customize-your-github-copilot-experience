# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI, a modern Python web framework. By the end of this assignment, you will be able to define routes, return JSON data, and validate request payloads.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a FastAPI application and add a basic endpoint that responds with a welcome message.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Define a root route using the `@app.get()` decorator
- Return a JSON response such as a greeting or status message
- Run the app locally with a development server

### 🛠️ Build a Resource Endpoint

#### Description
Create an API for managing a simple collection of items, such as books, tasks, or students.

#### Requirements
Completed program should:

- Define a list of sample items in memory
- Create a `GET` endpoint that returns all items
- Create a `POST` endpoint that adds a new item
- Return JSON data in a clear, structured format

### 🛠️ Add Validation and Dynamic Routes

#### Description
Use request models and path parameters to make the API more realistic and easier to use.

#### Requirements
Completed program should:

- Define a Pydantic model for item data
- Validate incoming request data before saving it
- Add a `GET` route for a single item using an item ID
- Return a helpful response when an item is not found

### 🛠️ Practice Clean API Design

#### Description
Refine your API so it is readable, reliable, and easy to extend.

#### Requirements
Completed program should:

- Use clear route names and descriptive response messages
- Keep related logic organized in small functions
- Avoid hardcoded logic that makes the API difficult to maintain
- Test the endpoints with a browser or API client

## 🧠 Skills Practiced

- Building web APIs in Python
- Designing REST-style endpoints
- Using Pydantic models for validation
- Handling JSON requests and responses
- Structuring backend code for readability and reuse
