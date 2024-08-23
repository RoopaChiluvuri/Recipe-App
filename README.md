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

<h5>Clone the Repository:</h5>
$ git clone https://github.com/RoopaChiluvuri/Recipe-App.git

<h5>Navigate to the Project Directory:</h5>
$ cd recipe-app

<h5>Create a Virtual Environment:</h5>
$ python3 -m venv env

<h5>Activate the Virtual Environment:</h5>
<b>On macOS and Linux:</b> $ source env/bin/activate
On Windows:

env\Scripts\activate
Install Dependencies:

pip install Django
Alternatively, if you have a requirements.txt file:

pip install -r requirements.txt
Apply Migrations:

python manage.py migrate
Create a Superuser:

python manage.py createsuperuser
Follow the prompts to set up the superuser credentials.
Run the Development Server:
python manage.py runserver
Access the Application:
Open your browser and navigate to http://localhost:8000 to view the app.
Access Django Admin at http://localhost:8000/admin/ using the superuser credentials.
Usage

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
