document.getElementById('add_item').addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('.my_list').appendChild(li);
});