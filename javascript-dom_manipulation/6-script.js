fetch('https://swapi-api.hbtn;io/api/poeple/5/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    document.querySelector('#character_name').textContent = data.name;
  });
