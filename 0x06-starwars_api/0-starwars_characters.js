#!/usr/bin/node
import { get } from "request";
const url =
  "https://swapi-api.alx-tools.com/api/films/" + process.argv[2] + "/?format=json";
get(url, function (response, body) {
  const film = JSON.parse(body.body);
  // debugging
  // console.log(film);
  // console.log(film.characters);
  character(film.characters);
});
const character = (people, i = 0) => {
  if (i === people.length) return;
  get(people[i], function (response, body) {
    // console.log(people[i]);
    console.log(JSON.parse(body.body).name);
    character(people, i + 1);
  });
};
