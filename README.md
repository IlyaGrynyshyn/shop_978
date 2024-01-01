# [978.ua](https://nine78-ua.onrender.com/) - Online Store

This project represents an online store. It's developed to offer various products across different categories for
convenient and straightforward online shopping.

## Project Overview

"shop_978.ua" is a web application that allows users to browse products, add them to their cart, and make purchases. The
app also provides user registration and login functionalities.

## Features

- Browse products catalog categorized into different sections.
- Add products to the cart for future purchases.
- Checkout and place orders.
- User registration and login functionalities.
- View order history to track previous purchases.

## Technologies Used

The "978.ua" project is developed using the following technologies:

- Django: Python-based web framework for building web applications.
- HTML/CSS/JavaScript: For frontend development and user interaction.
- Database: PostgreSQL

## Usage Instructions

Python must be already installed.

1. **Installation:**
    - Clone the repository to your local machine `https://github.com/IlyaGrynyshyn/shop_978`.
    - Create virtual environment `python3 -m venv venv`
    - Install the required dependencies using `pip install -r requirements.txt`.

2. **Running:**
    - Apply migrations `python manage.py migrate`
    - Start the server with `python manage.py runserver`.
    - Access the store via `http://localhost:8000` in your web browser.

3. **Registration/Login:**
    - To access all functionalities of the project, create super user and log in to your account.

## Planned Enhancements

Future enhancements for the project include:

- Additional payment and shipping options.
- Product search and filtering.
- Password recovery capabilities.
- Wish list

## Developer Commands

- `python manage.py makemigrations`: Create database migrations.
- `python manage.py migrate`: Apply migrations to the database.
- `python manage.py createsuperuser`: Create a site administrator.

## Contribution

If you have ideas or would like to contribute to the project, please fork the repository and create a pull request.

Thank you for your interest in the "shop_978.ua" project!
