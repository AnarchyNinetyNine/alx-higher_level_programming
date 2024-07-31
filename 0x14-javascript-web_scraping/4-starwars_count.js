#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  let count = 0;

  data.results.forEach((film) => {
    if (film.characters.some((url) => url.endsWith(`/${wedgeId}/`))) {
      count++;
    }
  });

  console.log(count);
});
