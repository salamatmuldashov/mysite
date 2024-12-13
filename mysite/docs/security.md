# Security Audit and Measures

This document outlines the security audit performed and the security measures implemented in the Django application. 

## 1. Security Middleware

A custom `SecurityMiddleware` was added to enforce essential security measures. The middleware provides the following protections:

### a) CSRF Protection
The middleware ensures that all POST requests are protected by CSRF tokens. If the CSRF token is missing or invalid, a CSRF error is triggered.


## 2. Secure Login and Registration Endpoints

The login and registration endpoints are secured with:

- **JWT Authentication**: Both the login and registration endpoints generate and return a JWT token after successful user authentication or registration.
- **Password Hashing**: Passwords are hashed using Django's `check_password` and stored securely.
- **Input Validation**: User inputs are validated using serializers to prevent invalid data and ensure secure user registration and login.

