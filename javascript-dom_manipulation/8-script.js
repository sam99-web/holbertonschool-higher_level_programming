document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })

    .then(function (data) {
      document.querySelector('#hello').textContent = data.hello;
    });
});
