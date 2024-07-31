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
  const characters = movie.characters; // Array of character URLs

  // Function to fetch character data
  function fetchCharacter (index) {
    if (index >= characters.length) return; // Base case: no more characters to fetch

    const characterURL = characters[index];

    request(characterURL, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse and print the character's name
      const character = JSON.parse(body);
      console.log(character.name);

      // Fetch the next character
      fetchCharacter(index + 1);
    });
  }

  // Start fetching characters
  fetchCharacter(0);
});
