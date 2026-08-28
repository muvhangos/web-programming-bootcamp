# Simple Service Booking System

## 1. Use Case

### Project Name

Simple Service Booking System

### Purpose

The Simple Service Booking System is a small web application that allows customers to book a service online.

The system helps a small service business manage customer bookings without using paper records or managing all bookings manually through phone calls or messages.

### Problem Statement

Small businesses often manage customer bookings manually. This can result in double bookings, lost information, and difficulty tracking customer requests.

This system provides a simple online solution where customers can create and view their bookings, while an administrator manages all bookings.

### Users of the System

The system has two user roles.

#### Customer

The customer can:

* Register an account
* Login and logout
* Create a service booking
* Select a booking date
* Enter a service description
* View their own bookings

#### Administrator

The administrator can:

* Login to the system
* View all bookings
* View customer information
* Approve or reject bookings
* Update booking status

### Main Features

The system will include:

1. User registration
2. User login and logout
3. Create a booking
4. View personal bookings
5. Administrator booking management
6. Booking status management

### Use Case Flow

#### Customer Booking

1. The customer opens the website.
2. The customer registers or logs in.
3. The customer creates a booking.
4. The customer enters the booking date and service description.
5. The system saves the booking.
6. The customer views their bookings.

#### Administrator Management

1. The administrator logs into the system.
2. The administrator views customer bookings.
3. The administrator reviews a booking.
4. The administrator updates the booking status.
5. The system saves the updated status.

### Benefits

The system:

* Reduces manual booking work.
* Keeps booking information organised.
* Allows customers to book services online.
* Allows administrators to manage bookings easily.
* Demonstrates Django authentication, database models, user roles, and administration.

### Scope

This project is intentionally kept small.

The system will focus on user authentication and service bookings. Online payments, notifications, and complex reports are outside the scope of this project.

---

# 2. Technology Design

The system will be developed using:

* Python
* Django
* HTML
* CSS
* SQLite Database
* GitHub

## System Architecture

```text
User
  ↓
Django Views
  ↓
Django Models
  ↓
SQLite Database
```

## User Roles

### Customer

* Register
* Login
* Create booking
* View own bookings

### Administrator

* Login
* View all bookings
* Update booking status

## Database Design

The application will use Django's built-in User model and one additional model.

### Booking

| Field               | Description                      |
| ------------------- | -------------------------------- |
| User                | Customer who created the booking |
| Booking Date        | Date requested                   |
| Service Description | Service requested                |
| Status              | Pending, Approved, or Rejected   |

---

# 3. Implementation

The system will be implemented using Django.

The application will include:

* User authentication
* Booking creation
* Booking history
* Django administration
* Booking status management

---

# 4. User Guide

## Customer

1. Register an account.
2. Login.
3. Create a booking.
4. Enter the booking date.
5. Enter the service required.
6. Submit the booking.
7. View your bookings.

## Administrator

1. Login to the Django administration system.
2. View all bookings.
3. Select a booking.
4. Change the booking status.
5. Save the changes.
