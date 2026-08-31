const http = require('http');
const fs = require('fs');
const path = require('path');

// Set the port we want the server to listen on
const PORT = 3000;

const server = http.createServer((req, res) => {
    
    fs.readFile(path.join(__dirname, 'index.html'), (err, content) => {
        // Handle the case where the file is missing or cannot be read
        if (err) {
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            return res.end('Error: index.html not found. Please ensure it is in the same directory.');
        }
        
        // Send a successful response with the HTML content
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(content);
    });
});

server.listen(PORT, () => {
    console.log(`Server successfully started!`);
    console.log(`Navigate to http://localhost:${PORT} in your web browser to view the Simple Finance Page.`);
});