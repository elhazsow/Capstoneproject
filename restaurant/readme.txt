# Api endpoints
- http://127.0.0.1:8000/restaurant/menu
- http://127.0.0.1:8000/restaurant/menu/{pk}
- http://127.0.0.1:8000/restaurant/booking/tables
- http://127.0.0.1:8000/restaurant/booking/tables/{pk}
- http://127.0.0.1:8000/restaurant/api-token-auth/

# Authentication
- Use the token obtained from the api-token-auth endpoint to authenticate requests to the booking endpoints.
- http://127.0.0.1:8000/restaurants/api-token-auth/ - POST - { "username": "testuser", "password": "lemon@123" } - returns token: "c977eeba6836cbf59a7eef398f2cbc41a1891eca"