# Project Statement

## Problem Statement

Small e-commerce sellers may have sales records but lack a simple
system to manage sales information and generate useful business insights.

## Project Scope

This project aims to develop a command-line Python application that
manages e-commerce products, orders, customers, and sales information
while providing basic sales analytics.

## Target Users

- Small online sellers
- Student entrepreneurs
- Small e-commerce businesses

## High-Level Features

- Product management
- Sales and order management
- Inventory management
- Customer information management
- Sales analytics
- Report generation

## Objectives

This project aims to make managing an e-commerce store more convenient for both employees and customers using only a CLI, without the use of a GUI. The project focuses mainly on managing products and their inventory, customers and orders, calculating sales, and providing basic analytics. It makes the process easier to maintain compared to managing everything manually.

## Proposed Solution

My project helps the user, either an employee or a customer, to access what they need easily while automatically recording the information they provide for future reference. Each function is predefined and helps the user get directly to their needs. The system also generates basic analytics automatically using the recorded data provided by the user. CSV files are used to store the data, which makes it easier to handle and maintain.

## System Modules

Each module used in this system is clearly defined to make the functions easily accessible and reduce errors while running the system.

1. **Products** - This module performs functions related to products, such as adding, updating, or removing a product, as well as viewing all product details or the details of a specific product.

2. **Inventory** - This module manages inventory details, such as adding, updating, or removing inventory, as well as viewing all inventory details or the specific inventory details of a product.

3. **Orders** - This module handles functions related to ordering a product, such as placing and cancelling an order, creating an order ID, viewing orders made by a customer, and viewing all orders received by the system.

4. **Customer** - This module manages customer details, including registration, login, getting or cancelling premium membership, creating a customer ID, updating customer details, and viewing premium customer information.

5. **Employee** - This module focuses on employee-related functions, mainly handling employee login.

6. **Analytics** - This module performs sales-related calculations such as total sales, total orders, best-selling product, low-stock products, and the number of premium customers.

7. **Reports** - This module is used to generate the sales analytics report and depends on the Analytics module for the required information.
8. **Validation** - This module checks whether a product exists so that inventory cannot be created for an unknown product. It also checks whether an inventory entry exists to prevent errors while placing or managing orders.

## Technologies Used

The project is developed using Python and runs through a Command Line Interface (CLI). CSV files are used for storing and managing the data required by the system. Visual Studio Code was used for developing the project, while Git and GitHub were used for version control and project management.

## Data Storage

The system uses CSV files to store the data related to products, inventory, customers, employees, and orders. The data is read from the CSV files when required and updated whenever a new record is added or an existing record is modified or removed. This allows the system to manage the data without using a separate database.

## Expected Outcome

The expected outcome of this project is to provide a simple command-line system for managing products, inventory, customers, and orders in an organized way. The system should allow employees and customers to perform their required functions easily while keeping the related information stored in CSV files. It should also provide basic sales analytics and reports from the recorded order data.

## Future Improvements

The project can be improved in the future by using a database instead of CSV files for better data management. A graphical or web-based interface can also be added to make the system more user-friendly. Other possible improvements include adding a shopping cart, online payment options, more advanced sales analytics, and better password security.
