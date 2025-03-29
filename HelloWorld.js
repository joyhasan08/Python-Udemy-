// Basic Javascript code to display "Hello, World!" in a web page

console.log("Hello, World!"); // This will log "Hello, World!" to the console
document.addEventListener("DOMContentLoaded", function() {
    const message = document.createElement("h1");
    message.textContent = "Hello, World!";
    document.body.appendChild(message);
});
// This code will create an h1 element with the text "Hello, World!" and append it to the body of the document when the DOM is fully loaded.
// This is a simple JavaScript program that displays "Hello, World!" in a web page.