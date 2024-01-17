# Bank System Using OOP with MySQL Database

This is a simple Bank System implemented using Object-Oriented Programming (OOP) in Python, with data storage handled by a MySQL database.

## Features

- **BankAccount Class**: Represents a bank account with basic functionalities like deposit, withdrawal, and balance display.

- **BankSystem Class**: Manages the interaction with the MySQL database, allowing for the creation of new accounts and retrieval of existing ones.

## Getting Started

### Prerequisites

- Python
- MySQL database

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Prashant2029/Bank.git
    cd BankSystem
    ```

2. Install the required Python libraries:

    ```bash
    pip install mysql-connector-python
    ```

3. Set up the MySQL database:
    - Create a new database named `BankSystem`.
    - Run the SQL script in `database_setup.sql` to create the `BankAccounts` table.

4. Update the MySQL connection details:
    - Open `bank_system.py` and replace the placeholder values in the `mysql.connector.connect` method with your actual MySQL database connection details.

### Usage

1. Run the example script:

    ```bash
    python bank_system.py
    ```

2. Explore the basic functionalities provided by the `BankAccount` and `BankSystem` classes.

## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
