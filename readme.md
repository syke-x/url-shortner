# API Endpoints Documentation

This document provides a complete list of the available API endpoints for [Your Project/API Name].

**Base URL:** `https://api.yourdomain.com/v1`

---

## 👥 Users

Endpoints related to user management and authentication.

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `GET` | `/users` | Retrieves a list of all users. | Yes |
| `GET` | `/users/{id}` | Retrieves details of a specific user. | Yes |
| `POST` | `/users` | Creates a new user. | No |
| `PUT` | `/users/{id}` | Updates an existing user's information. | Yes |
| `DELETE` | `/users/{id}` | Deletes a user. | Yes |

### User Endpoint Details

**`GET /users/{id}`**
* **Path Parameters:**
  * `id` (integer): The unique identifier of the user.
* **Response (200 OK):**
  ```json
  {
    "id": 1,
    "name": "Jane Doe",
    "email": "jane@example.com"
  }