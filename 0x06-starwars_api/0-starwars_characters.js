#!/usr/bin/node
// Import the request module for making HTTP requests
const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Define the base URL for the Star Wars API
const baseUrl = 'https://swapi-api.hbtn.io/api/';

// Make a GET request to fetch the movie data using the movie ID
request.get(`${baseUrl}films/${movieId}`, { json: true }, (err, res, body) => {
  // Handle any errors that occur during the request
  if (err) { return console.log(err); }
  // Extract the characters array from the response body
  const result = body.characters;
  // Debug line to print characters array (commented out)
  // console.log(result);

  // Start fetching individual character details
  actorsList(result);
});

// Recursive function to fetch and print character names in sequence
function actorsList (result, i = 0) {
  // Base case: if we've processed all characters, return
  if (i === result.length) return;

  // Make a GET request for each character URL
  request(result[i], { json: true }, (err, res, body) => {
    // Handle any errors that occur during character request
    if (err) { return console.log(err); }

    // Print the character's name
    console.log(body.name);
    // Recursively call actorsList for the next character
    actorsList(result, i + 1);
  });
}
