#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort();
  console.log(args[1]);
}
