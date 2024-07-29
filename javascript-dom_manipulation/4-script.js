document.getElementById('add_item').addEventListener('click', function() {
    const new_item = document.createElement('li');
    new_item.textContent = 'item';
    document.querySelector('ul.my_list').appendChild(new_item);
});