// static/js/scripts.js
function showBooks() {
    fetch("/books")
        .then(response => response.json())
        .then(data => {
            let output = "<h2>Available Books</h2>";
            for (let book in data) {
                output += `<p>${book}: ${data[book]} copies</p>`;
            }
            document.getElementById("output").innerHTML = output;
        })
        .catch(error => console.error('Error fetching books:', error));
}

function borrowBook() {
    const name = prompt("Enter your name:");
    const bookname = prompt("Enter the book name to borrow:");
    fetch("/borrow", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name, bookname: bookname })
    })
    .then(response => response.json())
    .then(data => document.getElementById("output").innerHTML = data.message)
    .catch(error => console.error('Error borrowing book:', error));
}

function returnBook() {
    const name = prompt("Enter your name:");
    const bookname = prompt("Enter the book name to return:");
    fetch("/return", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name, bookname: bookname })
    })
    .then(response => response.json())
    .then(data => document.getElementById("output").innerHTML = data.message)
    .catch(error => console.error('Error returning book:', error));
}

function donateBook() {
    const bookname = prompt("Enter the book name to donate:");
    fetch("/donate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ bookname: bookname })
    })
    .then(response => response.json())
    .then(data => document.getElementById("output").innerHTML = data.message)
    .catch(error => console.error('Error donating book:', error));
}

function viewLog() {
    fetch("/log")
        .then(response => response.json())
        .then(data => {
            let output = "<h2>Borrow/Return Log</h2>";
            data.forEach(record => {
                output += `<p>${record.Name} ${record.Status} "${record.Book}"</p>`;
            });
            document.getElementById("output").innerHTML = output;
        })
        .catch(error => console.error('Error fetching log:', error));
}
