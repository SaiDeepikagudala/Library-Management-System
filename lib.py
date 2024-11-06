
from flask import Flask, request, render_template, redirect, url_for, flash
from tabulate import tabulate

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Add a secret key for flash messages

class Library:
    def __init__(self, book_inventory):
        self.books = book_inventory  # Dictionary to keep track of book names and quantities
        self.borrow_return_log = []  # List to track borrowed and returned book details

    def displayAvailableBooks(self):
        return self.books

    def borrowBook(self, name, bookname):
        if bookname not in self.books or self.books[bookname] == 0:
            return f"{bookname} is not available at present."
        else:
            self.borrow_return_log.append({"Name": name, "Book": bookname, "Status": "Borrowed"})
            self.books[bookname] -= 1  # Reduce the count by 1
            return "Book issued. Please return before the due date."

    def returnBook(self, name, bookname):
        if bookname in self.books:
            self.books[bookname] += 1  # Increase the count by 1
        else:
            self.books[bookname] = 1  # Add the book if it was not in the collection
        self.borrow_return_log.append({"Name": name, "Book": bookname, "Status": "Returned"})
        return "Book returned: Thank you!"

    def donateBook(self, bookname):
        if bookname in self.books:
            self.books[bookname] += 1
        else:
            self.books[bookname] = 1
        self.borrow_return_log.append({"Name": "Donor", "Book": bookname, "Status": "Donated"})
        return f"Thank you for donating {bookname}!"

    def displayBorrowReturnLog(self):
        return self.borrow_return_log if self.borrow_return_log else None


# Initialize the library with some books
library = Library({
    "Science and Invention": 3,
    "Fiction": 5,
    "Economics": 2,
    "Deadpool": 1,
    "You Can Win": 4,
    "The Alchemist": 2
})

@app.route('/')
def index():
    available_books = library.displayAvailableBooks()
    borrow_return_log = library.displayBorrowReturnLog()
    return render_template('index.html', books=available_books, log=borrow_return_log)

@app.route('/borrow', methods=['POST'])
def borrow():
    name = request.form.get('name')
    bookname = request.form.get('bookname')
    message = library.borrowBook(name, bookname)
    flash(message)
    return redirect(url_for('index'))

@app.route('/return', methods=['POST'])
def return_book():
    name = request.form.get('name')
    bookname = request.form.get('bookname')
    message = library.returnBook(name, bookname)
    flash(message)
    return redirect(url_for('index'))

@app.route('/donate', methods=['POST'])
def donate():
    bookname = request.form.get('bookname')
    message = library.donateBook(bookname)
    flash(message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

