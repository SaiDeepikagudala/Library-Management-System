# Library Management System

A simple Library Management System built using Python and Flask. This system allows users to perform basic library operations such as borrowing, returning, and donating books. It also maintains a transaction log to track each book's status and user interactions.

## Features

- **View Available Books**: See the current inventory of books in the library.
- **Borrow a Book**: Users can borrow books from the library if available.
- **Return a Book**: Users can return previously borrowed books.
- **Donate a Book**: Users can add new books to the library's inventory.
- **Transaction Log**: Track all book transactions (borrowed, returned, donated) with user details.

## Technologies Used

- Python
- Flask
- HTML/CSS
- JavaScript (optional)
- Tabulate (for displaying logs in a formatted table)

## Prerequisites

- **Python 3.x** installed on your machine.
- **Flask**: You can install Flask using the following command:
  ```bash
  pip install Flask
  pip install tabulate

**Usage**
=========

**View Available Books**: The homepage displays a list of all books currently available in the library along with their quantities.

**Borrow a Book**: Enter your name and the book name you wish to borrow in the "Borrow Book" form. If the book is available, it will be issued to you, and the inventory will update.

**Return a Book**: Enter your name and the book name in the "Return Book" form. The book will be returned to the library, updating the inventory.

**Donate a Book**: Enter the name of the book you want to donate. The donated book will be added to the library's inventory.

**View Transaction Log**: The transaction log table displays a history of all borrow, return, and donation actions.


**Future Enhancements**
======================
Some ideas to expand this project:

User Authentication: Add user login/logout functionality.
Book Search: Implement a search feature for finding books.
Due Date Tracking: Add due date functionality for borrowed books.
Email Notifications: Send email notifications for overdue books or successful transactions.

