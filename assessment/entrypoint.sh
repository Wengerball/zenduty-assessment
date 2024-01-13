#!/bin/sh

# Exit the script in case of an error
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Initialize the database with default data
echo "Initializing the database with default PizzaBase, Cheese, and Topping data..."
python manage.py intialise_db

# Start the main process
echo "Starting main process..."
exec "$@"