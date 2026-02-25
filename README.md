🚗 Car Rental Management System
📌 Project Overview

The Car Rental Management System is a full-stack web application developed using Django.
The platform allows users to register, log in, browse available cars, book vehicles, choose payment methods, and manage their bookings efficiently.

The system also includes an administrative dashboard to manage cars, users, and booking records.
This project demonstrates backend development, database integration, and real-world booking workflow implementation.

🎯 Problem Statement

Traditional car rental systems often rely on manual processes, leading to:

Booking conflicts

Poor record management

Limited customer interaction

Inefficient vehicle tracking

This project provides a digital solution that automates booking, payment handling, and vehicle availability management.

🏗️ Project Architecture

The project follows Django’s MVT (Model-View-Template) architecture and is divided into multiple apps:

Accounts App – User authentication (Signup, Login)

Cars App – Car listing, pricing, availability management

Bookings App – Booking logic, payment status, booking confirmation

Dashboard App – Admin dashboard interface

🛠️ Tech Stack
Backend

Python

Django Framework

Frontend

HTML5

CSS3

Bootstrap

Database

MySQL

Tools

Git

GitHub

🔑 Core Features
👤 User Authentication

User Registration (Signup)

User Login & Logout

Secure session handling

🚘 Car Management

Display available cars

Car type & seating capacity

Price per day / fare calculation

Availability status control

📅 Booking System

Book a car with start & end time

Location tracking (start & end location fields)

Automatic total price calculation

Booking confirmation page

Booking success page

💳 Payment System

Payment method selection

Payment status tracking

Booking linked with payment status

📊 Admin Dashboard

Manage cars

Manage bookings

View booking status

Track customer records

🖼️ Media Management

Car image upload support

Static & media file configuration

🗂️ Database Design

The system uses MySQL as the relational database.

Major Models Include:

User

Car

Booking

Payment Status

Availability Status

Relationships are implemented using Django ORM with proper ForeignKey associations.

🔄 Booking Workflow

User registers or logs in

User views available cars

User selects car and booking details

System calculates total fare

User selects payment method

Booking is confirmed and stored in database

Payment status is updated

Admin can monitor through dashboard

🎓 My Role

Designed complete backend architecture using Django

Implemented booking logic and payment status handling

Designed database models and relationships

Integrated MySQL with Django

Managed media & static file handling

Developed admin dashboard features

Implemented real-world booking workflow logic

🚀 Future Enhancements

Online payment gateway integration (Razorpay/Stripe)

Email booking confirmation

Advanced filtering (price, car type)

Booking cancellation policy automation

Deployment on cloud platform (AWS / Render)

📈 Key Learning Outcomes

Multi-app Django project structuring

Real-world database schema design

Authentication & authorization handling

Booking workflow implementation

Payment state management

Admin panel customization

✨ This project reflects strong backend development skills and practical implementation of a real-world rental management system.
