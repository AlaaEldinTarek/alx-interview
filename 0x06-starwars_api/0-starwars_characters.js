#!/usr/bin/node

const request = require('request');
const ac = process.argv.slice(2);

request.get(`https://swapi-api.alx-tools.com/api/films/${ac}/`, async (_error, response, body) => {
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    const charac = await new Promise((resolve, reject) => {
      request(character, (errors, responses, bodys) => {
        if (errors) {
          reject(errors);
        } else {
          resolve(JSON.parse(bodys).name);
        }
      });
    });
    console.log(charac);
  }
});