OpenStockMate

OpenStockMate is an open-source and free component inventory management application.
About

This project is developed by the community at mekatronik.org/forum. The goal is to enable users to effectively manage their electronic component inventories.
Features

    Component inventory management
    Component inventory alert emails
    Registration emails
    Separate inventory page for each user
    180 days password expiration
    8-character case-sensitive password requirement
    Activation email

Installation

    Clone the project to your computer.

    bash


bash

cd OpenStockMate

Install the necessary dependencies.

bash

# Create a virtual environment if necessary
python -m venv venv          # Linux
venv\Scripts\activate        # Windows

# Activate the virtual environment
source venv/bin/activate     # Linux
venv\Scripts\activate        # Windows

# Install required packages
pip install -r requirements.txt

Create the database and start the application.

bash

    python manage.py migrate
    python manage.py runserver

    Open your browser and go to http://127.0.0.1:8000/.

Contribution

If you would like to contribute to the project, feel free to get involved! :)
License

This project is licensed under the [MIT License].
