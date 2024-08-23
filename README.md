<h1>Recipe App</h1>

<p>A Django-based recipe management application that supports creating, reading, updating, and deleting (CRUD) recipes. The app includes user authentication, custom pages, Bootstrap integration for styling, and sample data.</p>

<h2>Features</h2>

<h5>User Authentication:</h5> Register, login, and logout functionalities.<br/>
<h5>CRUD Operations:</h5> Create, read, update, and delete recipes.<br/>
<h5>Custom Pages:</h5> Home and About pages with titles and sample data.<br/>
<h5>Admin Interface:</h5> Manage recipes and users through Django Admin.<br/>
<h5>Responsive Design:</h5> Styled with Bootstrap for a responsive and modern UI.<br/>
<h5>Sample Data:</h5> Pre-populated with sample recipes for demonstration.<br/>

<h2>Technologies Used</h2>

Backend: Django
Database: SQLite (default; can be switched to PostgreSQL, MySQL, etc.)
Frontend: HTML, CSS, Bootstrap, Django Templates
Version Control: Git
Environment: Python 3.x


<h2>Steps to run the project in local</h2>

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
Open your browser and navigate to http://localhost:8000/ to view the app.

Access Django Admin at http://localhost:8000/admin/ using the superuser credentials.

