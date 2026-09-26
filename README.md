# E-Commerce Sales Analytics & Management System

A command-line Python application for managing e-commerce sales data,products,orders and generating useful sales insights.

## Project Status

Completed.
## Features
### Employee Features
- Manage Products
- Manage Inventory
- Manage Customers
- Manage Orders
- View Sales Analytics
- View Sales Report

### Customer Features
- Register and login
- View and search products
- Place orders
- View orders
- Cancel orders
- Get and cancel premium membership
- Update account details

## Project Structure
- `main.py` - Main program and menu system
- `src/` - Contains all the Python modules used.
- `data/` - Contains all CSV files used to store project data
- `README.md` - Project Documentation
- `.gitignore`- Files and folders ignored by Git
- `statement.md` - Project statement and details
### Python Modules

- `products.py` - Product management
- `inventory.py` - Inventory management
- `customer.py` - Customer registration, login and account management
- `employee.py` - Employee login
- `orders.py` - Order placement and cancellation
- `analytics.py` - Sales and product analytics
- `reports.py` - Sales report generation
- `validation.py` - Product and inventory validation
### Data Files

- `products.csv` - Product details
- `inventory.csv` - Product stock
- `customer.csv` - Customer details
- `employee.csv` - Employee login details
- `orders.csv` - Order records

## Requirements

- Python 3.14
- No external Python libraries are required.
- The project can be run from a terminal or command prompt.
## Setup and Run

1. Clone or download the repository.
2. Open the project folder in a terminal.
3. Make sure Python 3.14 is installed.
4. Run the following command:

```bash
`python main.py`
```

## How to Use

1. Run `main.py`.
2. Select Employee Login or Customer Login.
3. Employee accounts are pre-configured in `data/employee.csv` and can be added manually by the administrator.
4. New customers can register before logging in.
5. Employees can manage products, inventory, customers, orders, analytics, and reports.
6. Customers can view products, place and cancel orders, manage their account, and use premium membership.
7. Choose the logout or exit option when finished.

## Data Storage

The project uses CSV files to store and manage data.

- `products.csv` - Stores product details
- `inventory.csv` - Stores product stock quantities
- `customer.csv` - Stores customer account details
- `employee.csv` - Stores employee login details
- `orders.csv` - Stores order records

The CSV files are automatically updated when data is added, modified, or removed through the application.

## Future Improvements

- Use a database instead of CSV files for data storage.
- Add a graphical or web-based interface.
- Add a shopping cart for multiple products in one order.
- Add online payment functionality.
- Add more advanced sales analytics.
- Improve password security.