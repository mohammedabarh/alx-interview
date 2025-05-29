#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  if (res.statusCode !== 200) {
    process.exit(1);
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  function printCharacter(index) {
    if (index >= characters.length) {
      return;
    }
    request(characters[index], (error, response, characterBody) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);
        printCharacter(index + 1);
      } else {
        process.exit(1);
      }
    });
  }

  printCharacter(0);
});
