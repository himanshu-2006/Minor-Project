# Minor-Project
A simple and interactive library management system built using Python, CustomTkinter (CTk), and MySQL. This project is designed for librarians to manage books efficiently.

Features
Secure Login System
Add, Update, Borrow, Return, and Delete Books
View Logs and Book Records
MySQL Database Integration
Easy-to-Use CustomTkinter Interface
Login Credentials:
Username: [12,22,32]
Password: [156,157,158]


How to Use the System
Step 1: Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
Step 2: Create the Database
Install MySQL Server if not already installed.
Open MySQL Workbench or your preferred MySQL client.
Run the following SQL commands to set up the database:

CREATE DATABASE library_management;

USE library_management;

CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    total_quantity INT NOT NULL,
    available_quantity INT NOT NULL
);

CREATE TABLE transaction (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    book_name VARCHAR(255) NOT NULL,
    student_id INT NOT NULL,
    librarian_id INT NOT NULL,
    issued_date DATETIME NOT NULL,
    due_date DATE NOT NULL,
    return_date DATETIME,
    status ENUM('borrowed', 'returned') DEFAULT 'borrowed',
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

Step 3: Install Dependencies
Make sure you have Python installed.
Install required Python libraries using:
pip install customtkinter mysql-connector-python

Step 4: Run the Application
Navigate to the project folder and run:
python main.py



Future Enhancements
Add Fine Calculator
Two-Factor Authentication
Multi-Library Support
Feel free to contribute by submitting pull requests or reporting issues!

