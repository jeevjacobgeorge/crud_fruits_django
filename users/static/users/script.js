document.getElementById('search').addEventListener('input', function() {
    const query = this.value;
    fetch(`/users/search/?q=${query}`)
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('fruit-container');
            container.innerHTML = '';
            data.fruits.forEach(fruit => {
                const fruitCard = document.createElement('div');
                fruitCard.classList.add('fruit-card');
                fruitCard.innerHTML = `
                    <h2>${fruit.name}</h2>
                    <p><strong>Family:</strong> ${fruit.family}</p>
                    <p><strong>Order:</strong> ${fruit.order}</p>
                    <p><strong>Genus:</strong> ${fruit.genus}</p>
                    <p>Nutritional Content:</p>
                    <ul>
                        <li><strong>Calories:</strong> ${fruit.nutrition.calories}</li>
                        <li><strong>Fat:</strong> ${fruit.nutrition.fat}</li>
                        <li><strong>Sugar:</strong> ${fruit.nutrition.sugar}</li>
                        <li><strong>Carbohydrates:</strong> ${fruit.nutrition.carbohydrates}</li>
                        <li><strong>Protein:</strong> ${fruit.nutrition.protein}</li>
                    </ul>
                    <div class="btn-container">
                        <a href="/users/delete_fruit/${fruit.id}"><button class="delete-btn">Delete</button></a>
                        <a href="/users/update_fruit/${fruit.id}"><button class="delete-btn">Update</button></a>
                    </div>
                `;
                


                container.appendChild(fruitCard);
            });
            
            if (data.fruits.length === 0) {
                container.innerHTML = '<h2>No fruit found</h2>';
            }
        })
        .catch(error => {
            console.error('Error fetching fruits:', error);
            const container = document.getElementById('fruit-container');
            container.innerHTML = '<h2>Error loading fruits</h2>';
        });
});

function redirectToGoogle(query) {
    const url = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
    window.open(url, '_blank');
}




