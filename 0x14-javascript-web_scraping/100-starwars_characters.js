#!/usr/bin/node

const request = require('request'); // Module to make HTTP requests
const movieId = process.argv[2]; // Movie ID from command line argument
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`; // API URL for the movie

// Fetch movie details and log each character's name
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);

  movie.characters.forEach((characterURL) => {
    request(characterURL, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name); // Print character's name
    });
  });
});
