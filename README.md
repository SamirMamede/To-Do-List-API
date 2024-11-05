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
- Lists all tasks
- Returns 200 OK with task list

### POST /api/tasks/create/
- Creates new task
- Required field: title
- Optional fields: description, completed
- Returns 201 Created on success
- Returns 400 Bad Request if invalid

### GET /api/tasks/{pk}/
- Retrieves single task details
- Returns 200 OK with task data
- Returns 404 Not Found if invalid ID

### PUT /api/tasks/{pk}/
- Updates existing task
- Can update title, description, completed
- Returns 200 OK with updated data
- Returns 400 Bad Request if invalid
- Returns 404 Not Found if invalid ID

### DELETE /api/tasks/{pk}/
- Deletes task
- Returns 204 No Content on success
- Returns 404 Not Found if invalid ID

### Tests Coverage ✅
- View Tests:
  - Task listing (GET /api/tasks/)
  - Task creation:
    - Creation with minimal data (title only)
    - Creation with all fields
    - Creation with invalid data
  - Task detail operations:
    - Detail retrieval (GET /api/tasks/{id}/)
    - Detail retrieval for non-existent task
    - Task update (PUT /api/tasks/{id}/)
    - Task update with invalid data
    - Task deletion (DELETE /api/tasks/{id}/)
    - Task deletion for non-existent task
  - Response validations:
    - Status codes (200, 201, 204, 400, 404)
    - Response data structure and content
    - Task count verification
  
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

## Getting Started 🚀

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository
2. Navigate to the project root directory
3. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate # Linux/MacOS
or
venv\Scripts\activate # Windows
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run migrations
```bash
python manage.py migrate
```
6. Start development server
```bash
python manage.py runserver
```

## Testing 🧪
To run the tests, navigate to the project root directory and use the following command:
```bash
python manage.py test api.tests
```