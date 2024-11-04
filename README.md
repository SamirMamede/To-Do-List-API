# To-Do List API 📝

A simple task management API built with Django and Django REST Framework.

## Features ✨

- Create, read, update, and delete tasks. ✅
- Mark tasks as completed. ✔️
- List all tasks. 📋

## Technologies ⚙️

- Python 🐍
- Django 🌐
- Django REST Framework 📦
- SQLite 🗄️

## Project Structure 🏗️

### Models
- Task model with fields:
  - title (required)
  - description (optional) 
  - completed status
  - created_at timestamp
  - completed_at timestamp

## API Endpoints 🛠️

### GET /api/tasks/
- Lists all tasks in the system
- Returns task details including title, description, completion status and timestamps
- Success Response: 200 OK

### POST /api/tasks/create/
- Creates a new task
- Required fields:
  - title: string
- Optional fields:
  - description: string
  - completed: boolean
- Success Response: 201 Created
- Error Response: 400 Bad Request (invalid data)

### Tests Coverage ✅
- View Tests:
  - Task listing (GET /api/tasks/)
  - Task creation with minimal data
  - Task creation with all fields
  - Task creation with invalid data
  - Response status code validation
  - Response data validation
  
- Serializer Tests:
  - Task serialization validation
  - Task deserialization validation
  - Required fields validation
  - Optional fields handling

- Model Tests:
  - Task creation
  - Task string representation
  - Automatic completed_at timestamp setting
  - Completed status toggle behavior
  - Field constraints validation