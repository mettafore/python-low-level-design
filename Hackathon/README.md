# Hackathon Low Level Design

This project is a low level design for a Hackathon event. It includes the backend API design and implementation.

## API Endpoints

The API includes the following endpoints:

- POST /payments - Initiate a new payment
- GET /payments/{payment_id} - Get details of a specific payment (For Buyer/Admin/Seller involved)
- PUT /payments/{payment_id} - Update details of a specific payment (For Admin/Seller involved)
- DELETE /payments/{payment_id} - Delete a specific payment (For Admin/Seller involved)
- GET /books/search - Search for books
- GET /books/category/{category_name} - Browse books by category

## Setup

To setup the project, follow these steps:

1. Clone the repository
2. Install the dependencies using pip
3. Run the main.py file to start the server

## Contributing

Contributions are welcome. Please make a pull request.

## License

This project is licensed under the MIT License.
