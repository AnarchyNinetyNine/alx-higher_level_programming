#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    args[i] = parseInt(args[i], 10);
  }

  args.sort((a, b) => b - a);
  console.log(args[1]);
}
