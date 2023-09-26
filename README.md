# police-station-database-management-system

 
1. Introduction  :
   
The Criminal Records Management System is a Python-based graphical user interface (GUI) application built using the tkinter library. It allows authorized users to manage criminal records and investigation officer data in an Oracle database. This system provides features such as inserting records, displaying records, deleting records, and dropping database tables.


2. Prerequisites:
   
Before using the Criminal Records Management System, ensure that you have the following prerequisites in place:
- Python installed on your system (Python 3.x recommended).
- The tkinter library for GUI components.
- The cx_Oracle library for connecting to the Oracle database.
- An Oracle database server with appropriate credentials and privileges.
- An understanding of the database structure and schema.


3. Installation:

- Install the required dependencies using pip:
   ```bash
   pip install cx_Oracle```

   
4. Usage:

    Login 
    1. Run the `login.py` script to start the application.
    2. Enter the username and password in the login window.
    3. Click the "Login" button.
    4. If the credentials are correct, you will be granted access to the main interface.
 
    Main Interface 
    - After successful login, you will be presented with the main interface.
    - The main interface consists of two tabs: "Crime Records" and "Investigation Officers."
    - You can switch between tabs to manage criminal records and officers' data.
 
    Database Operations 
 
      Insert Data
 
         - In either the "Crime Records" or "Investigation Officers" tab, fill in the required information in the input fields.
         - Click the "Insert Data" button to add a new record to the database.
 
      Display Records
 
         - Click the "Display Records" button to retrieve and display all records from the database in the respective table.
 
      Delete All Records
 
         - Click the "Delete All Records" button to remove all records from the database.
         
      Drop Tables
 
         - Click the "Drop Tables" button to delete the database tables. (Use with caution, as it deletes all data.)

 
 5 . Dependencies:
 
The project relies on the following dependencies:
- Python (3.x recommended)
- tkinter library
- cx_Oracle library

