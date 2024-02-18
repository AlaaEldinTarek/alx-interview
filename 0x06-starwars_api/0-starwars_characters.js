#!/usr/bin/node

const request = require("request");
const url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];
request(url, async (error, response, body) => {
  if (error) console.log(error);
  else {
    const result = JSON.parse(body).characters;
    for (const charId of result) {
      await new Promise((resolve, reject) => {
        request(charId, (error, response, body) => {
          if (error) reject(error);
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  }
});
