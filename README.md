# OpenStockMate

OpenStockMate is an open-source and free component inventory management application.

## About

Developed by the [www.mekatronik.org/forum](https://mekatronik.org/forum) community, OpenStockMate is designed to empower users in effectively managing their electronic component inventories.

## Features

- **Component Inventory Management:** Easily manage your electronic component inventory.
- **Component Inventory Alert Emails:** Receive alerts about your component stock.
- **Registration Emails:** Seamless user registration with confirmation emails.
- **Separate Inventory Page for Each User:** Personalized inventory management for every user.
- **Password Security:**
  - 180 days password expiration
  - 8-character case-sensitive requirement
  - Activation email for added security
  

## Installation

1. Clone the project to your computer.
2. download or git clone....

**Navigate to the Project Directory:**

    ```bash
    cd OpenStockMate
    ```

3. **Install Dependencies:**

    ```bash
    # Create and activate virtual environment (if necessary)
    python -m venv venv       # Linux
    venv\Scripts\activate     # Windows

    # Install required packages
    pip install -r requirements.txt
    ```

4. **Create the Database and Start the Application:**

    ```bash
    python3 manage.py migrate
    python3 manage.py runserver
    ```

5. **Open the Application in Your Browser:**

    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Contribution

If you'd like to contribute to the project, your involvement is welcome! Feel free to join and contribute.

## License

This project is licensed under the [MIT License].

---

Feel free to all enjoy

NOW MODELS
https://github.com/ixnur/OpenStockMate/blob/main/models.png
