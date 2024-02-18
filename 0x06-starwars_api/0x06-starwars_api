#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line in the same order of the list “characters”
// in the /films/ response
// You must use the Star wars API
// You must use the module request

// Require request which includes put() function
const request = require("request");
// To request, we need to concatenate the api with the endpoint
const url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

request(url, (error, response, values) => {
  if (error) {
    console.log(error);
  } else {
    // Store the results
    const results = JSON.parse(values).characters;
    showResults(results, 0);
  }
});

function showResults(results, index) {
  if (index === results.length) {
    return;
  }
  request(results[index], async (error, response, values) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(values).name);
      index += 1;
      showResults(results, index);
    }
  });
}
