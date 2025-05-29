#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  if (res.statusCode !== 200) {
    process.exit(1);
  }
  const film = JSON.parse(body);
  const characters = film.characters;

  function printCharacter(i) {
    if (i >= characters.length) {
      return;
    }
    request(characters[i], (error, response, charBody) => {
      if (error) {
        console.error(error);
        process.exit(1);
      }
      if (response.statusCode !== 200) {
        process.exit(1);
      }
      const character = JSON.parse(charBody);
      console.log(character.name);
      printCharacter(i + 1);
    });
  }

  printCharacter(0);
});
