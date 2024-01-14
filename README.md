# zenduty-assessment

Building a secure and scalable RESTful API that allows users to add pizzas and create a order, they can also be able to track the order.

## Framework and database

- This API is built using Django Rest Framework (DRF), a powerful and flexible toolkit for building APIs in Django.

- PostgreSQL is used as the database for storing data. MYSQL Development Server docker image was causing issues so I used postgresSQL

## Unit and Integration Testing

- The API includes comprehensive unit and integration tests to ensure correctness and reliability of endpoints.

## Getting Started

To run this project locally, follow these steps:

1. Docker Build Command:

    ```bash
    docker-compose build

2. Run the containers in detached mode:

    ```bash
    docker-compose up -d

3. Run tests.py:

    ```bash
    docker-compose run web python manage.py test 

## APIs and cURL Requests

1. cURL Request for user to add pizzas and create an order

    ```bash
    curl --location --request POST 'http://localhost:8000/api/pizza-order' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "pizzas":[
            {
                "pizza_base": "THIN-CRUST",
                "cheese": "MOZZARELLA",
                "toppings": ["PEPPERONI", "MUSHROOMS", "ONIONS", "SAUSAGE", "BACON"]
            },
            {
                "pizza_base": "NORMAL",
                "cheese": "MOZZARELLA",
                "toppings": ["PEPPERONI", "BLACK_OLIVES", "ONIONS", "SAUSAGE", "BACON"]
            }
        ]
    }'

2. cURL Request to track an order

    ```bash
    curl --location --request GET 'http://localhost:8000/api/tracker-order/?order_id=:id'
