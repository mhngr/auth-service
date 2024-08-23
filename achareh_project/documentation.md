# Achareh Project API Documentation

## Overview

This API is designed to handle user registration, login, and OTP verification using a mobile number. It is built using Django and Django REST Framework.

## Base URL

`http://localhost:8000/auth/`

## Endpoints

### 1. User Registration

- **URL**: `/register/`
- **Method**: `POST`
- **Headers**: 
  - `Content-Type: application/json`
- **Request Body**:

  ```json
  {
      "mobile": "1234567890",
      "password": "securepassword",
      "first_name": "John",
      "last_name": "Doe",
      "email": "john.doe@example.com"
  }
- **Success Response**:
  - `Code: 201 CREATED`

- **Content**:
  ```json
   {
    "message": "User registered successfully."
   }
  ```

### 2. OTP Generation
- **URL**: `/otp/`

- **Method**: `POST`

- **Headers**:

  - `Content-Type: application/json`
- **Request Body**:

```json

{
    "mobile": "1234567890"
}
```
- **Success Response**:

  - `Code: 201 CREATED`

  - Content:

```json
{
    "message": "OTP sent successfully."
}
```