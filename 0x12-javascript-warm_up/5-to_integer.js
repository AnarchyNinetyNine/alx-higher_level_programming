#!/usr/bin/node

const process = require('process');
const numArg = parseInt(process.argv[2], 10);
if (isNaN(numArg)) {
  console.log('Not a number');
} else {
  console.log('My number:', numArg);
}
