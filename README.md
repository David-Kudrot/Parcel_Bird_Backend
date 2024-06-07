# ParcelBird Food Delivery App - Backend

Welcome to the backend repository for ParcelBird, your go-to food delivery app! This backend is built using Django REST framework and provides all the necessary APIs for user management, restaurant browsing, cart management, and order processing.

## Features

### User Management
- **User Registration**: New users can register an account.
  - [Register](https://parcelbird.netlify.app/register)
- **User Login**: Existing users can log in using their credentials.
  - [Login](https://parcelbird.netlify.app/login)

### Restaurant Browsing and Ordering
- **Home Page**: Users can browse through a list of available restaurants.
  - [Home Page](https://parcelbird.netlify.app/?fbclid=IwAR0gb3ygOBdzDtaXE4W76N6AnyH2puRE24zV1i0K6seEz80B0LwHe37kM1g)
- **Shop**: Click on a restaurant to view its menu and other details.
  - [Shop](https://parcelbird.netlify.app/shop)
- **Product Details**: Users can view details of specific products.
  - [Product Details](https://parcelbird.netlify.app/detail.html?id=2)
- **Add to Cart**: Users can add items to their cart from the restaurant's menu.

### Cart and Order Management
- **View Cart**: Users can view the items added to their cart.
  - [Cart Items](https://parcelbird.netlify.app/cart.html)
- **Edit Cart**: Users can modify the quantity of items in their cart or remove items.
- **Checkout**: Users can proceed to purchase the items in their cart.
  - [Checkout](https://parcelbird.netlify.app/cart)
- **Order**: Users can place an order for the items in their cart.
  - [Order](https://parcelbird.netlify.app/checkout)

### Payment System
- **Payment Integration**: Secure payment system integrated for processing orders.
  - [Payment](https://parcelbird.netlify.app/payment.html)
  - [SslCommerz](https://sandbox.sslcommerz.com/EasyCheckOut/testcdeb1ecb957f48f31c2de448f0e7dfaf4da)
  - [Successful Payment](http://127.0.0.1:8000/api/payment/paymentSuccessful/JTKNSURFYB/9/)

### Contact
- **Contact Us**: Users can reach out for support or inquiries.
  - [Contact Us](https://parcelbird.netlify.app/contact)

## API Endpoints

Replace the Netlify links with the following backend API base URL: `https://parcel-bird-backend-ykce.onrender.com/api/`

### User Management
- `POST /api/register/` - Register a new user
- `POST /api/login/` - User login

### Restaurant Browsing
- `GET /api/restaurants/` - List all restaurants
- `GET /api/restaurants/:id/` - Get details of a specific restaurant

### Cart Management
- `GET /api/cart/` - View cart items
- `POST /api/cart/add/` - Add item to cart
- `PUT /api/cart/update/` - Update cart item
- `DELETE /api/cart/remove/` - Remove item from cart

### Order Management
- `POST /api/order/` - Place an order
- `GET /api/order/:id/` - Get details of a specific order

### Payment
- `POST /api/payment/` - Process payment
- `GET /api/payment/success/:transaction_id/` - Handle successful payment

## Getting Started

### Prerequisites
- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/parcelbird-backend.git
    ```
2. **Navigate to the project directory**
    ```bash
    cd parcelbird-backend
    ```
3. **Create a virtual environment**
    ```bash
    python3 -m venv venv
    ```
4. **Activate the virtual environment**
    ```bash
    source venv/bin/activate
    ```
5. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
6. **Set up environment variables**
    - Create a `.env` file in the root directory
    - Add the following variables to the `.env` file:
      ```
      DB_NAME=your_db_name
      DB_USER=your_db_user
      DB_PASSWORD=your_db_password
      DB_HOST=your_db_host
      DB_PORT=your_db_port
      SECRET_KEY=your_secret_key
      ```

7. **Run migrations**
    ```bash
    python manage.py migrate
    ```
8. **Start the server**
    ```bash
    python manage.py runserver
    ```

### Running the App

- **API**: The server will be running on `http://localhost:8000/api/`

## Project Structure


## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

Thank you to all our users and contributors for making ParcelBird possible!

---

Enjoy using ParcelBird! If you have any questions or feedback, please don't hesitate to reach out.

Happy ordering!

---
