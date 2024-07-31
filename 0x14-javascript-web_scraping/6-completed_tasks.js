#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const users = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);

  todos.forEach(todo => {
    if (todo.completed) {
      if (users[todo.userId]) {
        users[todo.userId] += 1;
      } else {
        users[todo.userId] = 1;
      }
    }
  });

  console.log(users);
});
