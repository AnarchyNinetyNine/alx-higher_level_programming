#!/usr/bin/node

const request = require('request'); // Ensure the 'request' module is installed
const movieId = process.argv[2]; // Get movie ID from command-line arguments
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`; // URL to fetch movie details

// Fetch the movie details
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the movie data
  const movie = JSON.parse(body);

  // Fetch each character's data
  movie.characters.forEach((characterURL) => {
    request(characterURL, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse and print the character's name
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
