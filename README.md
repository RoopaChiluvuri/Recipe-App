<h1>Recipe App</h1>

<p>A Django-based recipe management application that supports creating, reading, updating, and deleting (CRUD) recipes. The app includes user authentication, custom pages, Bootstrap integration for styling, and sample data.</p>

<h2>Features</h2>
User Authentication: Register, login, and logout functionalities.
CRUD Operations: Create, read, update, and delete recipes./n
Custom Pages: Home and About pages with titles and sample data.
- Admin Interface: Manage recipes and users through Django Admin.
- Responsive Design: Styled with Bootstrap for a responsive and modern UI.
- Sample Data: Pre-populated with sample recipes for demonstration.

<h2>Technologies Used</h2>
Backend: Django
Database: SQLite (default; can be switched to PostgreSQL, MySQL, etc.)
Frontend: HTML, CSS, Bootstrap, Django Templates
Version Control: Git
Environment: Python 3.x


<h2>Steps</h2>

<h4>Clone the Repository:</h4>
$ git clone https://github.com/RoopaChiluvuri/Recipe-App.git

<h4>Navigate to the Project Directory:</h4>
$ cd recipe-app

<h4>Create a Virtual Environment:</h4>
$ python3 -m venv env

<h4>Activate the Virtual Environment:</h4>
<h4>On macOS and Linux:</h4> $ source env/bin/activate
<h4>On Windows:</h4> $ env\Scripts\activate

<h4>Install Dependencies:</h4> $ pip install Django

<h4>Apply Migrations:</h4> $ python manage.py migrate

<h4>Create a Superuser:</h4> $ python manage.py createsuperuser

<h4>Follow the prompts to set up the superuser credentials.</h4>
<h4>Run the Development Server:</h4> $ python manage.py runserver


<h4>Access the Application:</h4>
Open your browser and navigate to http://localhost:8000 to view the app.

Access Django Admin at http://localhost:8000/admin/ using the superuser credentials.

<h5>Usage</h5>
Home and About Pages:
The application includes custom Home and About pages with titles and sample data.
Navigate to the Home page at http://localhost:8000/ and About page at http://localhost:8000/about/.
User Accounts:
Superuser: Created during installation for administrative tasks.
Test User:
Username: test
Password: test@123
Use these credentials to log in and test user-specific functionalities.
Managing Recipes:
Creating Recipes:
Use the "Add Recipe" button to create new recipes.
Viewing Recipes:
The Home page lists all recipes. Click on a recipe to view its details.
Editing and Deleting Recipes:
From the recipe detail page, you can edit or delete the recipe.
Django Admin:
Access Django Admin at http://localhost:8000/admin/ to manage recipes and users directly.
Templates and Styling:
HTML templates are located in the templates/ directory.
Bootstrap is integrated for responsive and aesthetic design.
