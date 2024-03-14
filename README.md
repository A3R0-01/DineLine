# DineLine API

## Introduction
This repository contains a powerful RESTful API built with Django, PostgreSQL, and JWT authentication. It provides a comprehensive and scalable solution for building robust web applications. This README file will guide you through the setup, features, and usage of this incredible API.

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Installation
To get started with this API, follow these steps:

1. Clone the repository to your local machine:
   git clone https://github.com/A3R0-01/Django-Restaurant-Backend-
2. Navigate to the project directory:
   cd Django-Restaurant-Backend-
3. Create a virtual environment:
   python3 -m venv venv
4. Activate the virtual environment:
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For Unix or Linux:
  ```
  source venv/bin/activate
  ```
5. Install the required dependencies:
  ```
  pip install -r requirements.txt
  ```
6. Set up the PostgreSQL database:
- Create a new database in PostgreSQL.
- Configure the database settings in the `settings.py` file.
7. Run the database migrations:
  python manage.py migrate

## Features
- **JWT Authentication**: Secure user authentication and authorization using JSON Web Tokens.
- **User Management**: Create, update, and delete user accounts with different permission levels.
- **Endpoint Authorization**: Restrict access to certain endpoints based on user roles and permissions.
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on various resources.
- **Validation and Error Handling**: Handle input validation and provide comprehensive error messages.
- **Pagination and Filtering**: Retrieve data in paginated form and apply filters for efficient data retrieval.

## Authentication
This API uses JSON Web Tokens (JWT) for authentication. To access protected endpoints, you need to include the JWT token in the `Authorization` header of your requests. The token can be obtained by authenticating with valid credentials using the `/auth/login/` endpoint. The generated token should be included in subsequent requests as follows:
Authorization: Bearer <token>

## Endpoints
The API provides the following endpoints:

- `/auth/register/`: Register a new user.
- `/auth/login/`: Obtain an authentication token.
- `/auth/logout/`: Blacklist the current token to log out.
- `/users/`: Manage user accounts (CRUD operations).
- `/posts/`: Manage blog posts (CRUD operations).
- `/comments/`: Manage comments on blog posts (CRUD operations).

For detailed information about request formats, response structures, and required permissions, please refer to the API documentation or interact with the API using tools like Postman or cURL.
