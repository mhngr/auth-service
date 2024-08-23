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
      "first_name": "Mahnegar",
      "last_name": "Eskandari",
      "email": "moon@example.com"
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
### 3. OTP Verification
- **URL**: `/verify-otp/`

- **Method**: `POST`

- **Headers**:

  - `Content-Type: application/json`
- **Request Body**:

```json

{
    "mobile": "1234567890",
    "otp_code": "123456"
}
```
- **Success Response**:

  - `Code: 200 OK`

  - Content:

```json

{
    "message": "OTP verified successfully."
}
```
### 4. User Login
- **URL**: `/login/`

- **Method**: `POST`

- **Headers**:

  - `Content-Type: application/json`
  - Request Body:

```json

{
    "mobile": "1234567890",
    "password": "securepassword"
}
```
- **Success Response**:

  - `Code: 200 OK`

  - Content:

```json

{
    "token": "your_token_here"
}
```
### Notes
- **Ensure the API is running locally on localhost:8000 before testing with Postman.**
- **Replace 1234567890 and other sample values with actual data as needed for testing.**
- **In case of authentication failures or invalid input, appropriate error messages and status codes will be returned.**

### How to Run the API
1. Clone the repository and navigate to the project directory.
 
2. Install the required dependencies using pip install -r requirements.txt.
 
3. Apply migrations using python manage.py migrate.

4. Run the server using python manage.py runserver.

5. Use Postman or any API testing tool to interact with the endpoints.

### Postman Collection
A Postman collection has been provided to help test the API endpoints. You can use this collection to interact with the API. Import the `achareh_project_postman_collection.json` file into Postman to get started.

### Example Postman Requests
#### 1. User Registration Request
- **Method**: `POST`

- **URL**: `http://localhost:8000/auth/register/`

- **Headers**:

  - `Content-Type: application/json`
  - Body:

```json

{
    "mobile": "1234567890",
    "password": "securepassword",
    "first_name": "Mahnegar",
    "last_name": "Eskandari",
    "email": "moon@example.com"
}
```
#### 2. OTP Generation Request
- **Method**: `POST`

- **URL**: `http://localhost:8000/auth/otp/`

- **Headers**:

  - Content-Type: `application/json`
  - Body:

```json

{
    "mobile": "1234567890"
}
```
#### 3. OTP Verification Request
- **Method**: `POST`

- **URL**: `http://localhost:8000/auth/verify-otp/`

- **Headers**:

  - `Content-Type: application/json`
  - Body:

```json

{
    "mobile": "1234567890",
    "otp_code": "123456"
}
```
#### 4. User Login Request
- **Method**: `POST`

- **URL**: `http://localhost:8000/auth/login/`

- **Headers**:

  - `Content-Type: application/json`
  - Body:

```json

{
    "mobile": "1234567890",
    "password": "securepassword"
}
```