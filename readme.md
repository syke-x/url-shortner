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

## URL
Endpoints related to URL management and authentication 

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :---: |
| `GET` | `/urls` | Retrieves a list of all urls. | Yes |
| `GET` | `/users/{user_id}/urls` | Retrieves URLs of a specific user. | Yes |
| `POST` | `/users/{user_id}/url` | Creates a new url | No |
| `DELETE` | `/users/{user_id}/{id}` | Deletes a url. | Yes |

