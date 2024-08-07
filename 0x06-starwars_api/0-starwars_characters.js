#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the base URL for the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the Star Wars API to get details about the movie
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body as JSON
  const movie = JSON.parse(body);

  // Iterate through the list of character URLs
  const characterUrls = movie.characters;
  characterUrls.forEach((url) => {
    // For each character URL, make a request to get the character's details
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the response body as JSON
      const character = JSON.parse(body);

      // Print the character's name
      console.log(character.name);
    });
  });
});
