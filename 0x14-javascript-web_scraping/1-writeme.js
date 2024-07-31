#!/usr/bin/node

const fs = require('fs');

// Get the file path and content from the arguments
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) console.error(err);
});
