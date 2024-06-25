# Fruit Information Website

## Project Overview
This project is a dynamic Django-based website designed to showcase information about various fruits, emphasizing their nutritional content. Users can seamlessly navigate, search, add, edit, and delete fruit details through a user-friendly interface.

## Features
- Display fruit details including family, order, genus, and nutritional content.
- Search functionality with real-time filtering using AJAX.
- Add new fruit entries with associated nutritional information.
- Edit existing fruit details.
- Delete fruit entries with confirmation.
- User authentication (login and registration).

## Requirements
- Python 3.8+
- Django 4.0+
- pip
- pip-tools

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/your-username/fruit-information-website.git
cd fruit-information-website
```

### Set Up Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Dependencies
```bash
pip install pip-tools
pip-sync requirements.txt dev-requirements.txt
```

### Apply Migrations
```bash
python manage.py migrate
```

### Run the Development Server
```bash
python manage.py runserver
```

## Usage

### Access the Website
Open your browser and go to `http://127.0.0.1:8000/` to access the website.

### Admin Interface
To manage the database directly, use the Django admin interface:
1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
2. Access the admin interface at `http://127.0.0.1:8000/admin/`.

### Adding, Editing, and Deleting Fruits
- Navigate to the fruit list page to see all fruits.
- Use the search bar to filter fruits in real-time.
- Click "Add Fruit" to add a new fruit entry.
- Click the edit icon next to a fruit to edit its details.
- Click the delete button to delete a fruit (confirmation required).

### User Authentication
- Register a new account or log in with existing credentials.
- The login and registration forms include placeholders for user convenience.

## Project Structure
```
fruit-information-website/
├── users/
│   ├── static/
│   │   ├── users/
│   │   │   ├── main.css
│   │   │   ├── auth.css
│   ├── templates/
│   │   ├── users/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── add_fruit.html
│   │   │   ├── update_fruit.html
│   │   │   ├── delete_fruit.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── requirements.txt
├── dev-requirements.txt
└── README.md
```

## CSS Customization
The project uses `auth.css` for login and registration pages and `main.css` for the rest of the site. Both CSS files are located under `users/static/users/`.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Django documentation
- Stack Overflow community

## Contact
For any inquiries or support, please contact [jeevjacobgeorge@gmail.com].
```

Feel free to replace placeholders like `https://github.com/your-username/fruit-information-website.git` and `your-email@example.com` with actual data relevant to your project. This README provides a structured and informative guide to set up, use, and contribute to your Django project.