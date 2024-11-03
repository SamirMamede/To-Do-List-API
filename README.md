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

### Tests Coverage ✅
- Model Tests:
  - Task creation with default values
  - String representation
  - Task completion/uncompletion behavior
  - Task updates without affecting completion status

- Serializer Tests:
  - Field validation
  - Required fields checking
  - Data serialization

- View Tests:
  - Task listing (GET /api/tasks/)

## Development Status 🚧

The project currently has:
- Complete data model implementation
- Basic task listing functionality
- Comprehensive test coverage for models and serializers
- Initial API endpoint for listing tasks