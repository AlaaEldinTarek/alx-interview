#!/usr/bin/node
const request = require("request");

const argv = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

function doRequest(characters, counter) {
  if (counter === 0) {
    return;
  }
  request(characters[0], function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const infoCharacter = JSON.parse(body);
    console.log(infoCharacter.name);
    doRequest(characters.slice(1), counter - 1);
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const info = JSON.parse(body);
  const infoCharacters = info.characters;
  doRequest(infoCharacters, infoCharacters.length);
});
