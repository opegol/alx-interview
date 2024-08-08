#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printFilmOrder(characters, 0);
  }
});

function printFilmOrder (c, i) {
  req(c[i], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (c.length > i + 1) {
        printFilmOrder(c, i + 1);
      }
    }
  });
}
