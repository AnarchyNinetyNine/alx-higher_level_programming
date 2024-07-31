#!/usr/bin/node

// Import the request module
const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const [url, filePath] = process.argv.slice(2);

// Check if URL and file path are provided
if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}

// Fetch the webpage content
request(url, (error, response, body) => {
  if (error) {
    console.error(`Error fetching the URL: ${error.message}`);
    process.exit(1);
  }

  // Write the content to the specified file with UTF-8 encoding
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(`Error writing to file: ${err.message}`);
      process.exit(1);
    }
  });
});
