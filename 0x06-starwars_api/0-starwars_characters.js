#!/usr/bin/node
const request = require('request');

// Check if movie ID is provided
if (process.argv.length !== 3) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.hbtn.io/api/films/';

// Promisify request to handle async operations better
const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) reject(error);
      else if (response.statusCode !== 200) {
        reject(new Error(`Status Code: ${response.statusCode}`));
      } else resolve(body);
    });
  });
};

// Main async function to handle the character fetching
async function getCharacters(movieId) {
  try {
    // Get movie data
    const movie = await makeRequest(`${baseUrl}${movieId}`);
    const characters = movie.characters;

    // Fetch and print characters in order
    for (const characterUrl of characters) {
      try {
        const character = await makeRequest(characterUrl);
        console.log(character.name);
      } catch (error) {
        console.error(`Error fetching character: ${error.message}`);
      }
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
}

// Execute the main function
getCharacters(movieId);
