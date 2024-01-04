#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const count = filmsData.reduce((total, film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        return total + 1;
      }
      return total;
    }, 0);

    console.log(count);
  }
});
