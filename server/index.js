// index.js
const express = require('express');   // import express
const app = express();                // create express app
const PORT = 5000;                    // server port

// Example route
app.get('/', (req, res) => {
  res.send('Server is running!');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
