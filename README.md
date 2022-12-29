libraryManagement
poc for api usage in django framework through library management tools
Rough outline
''' Have a rest api with endpoints for User creation Book checkout Book return Book creation

Use a postgres database to store the users, books, checkouts Only allow users tp check out 3 books at a time in due date Keep trak of which books are checked out so you can't loan out books that aren't in stock

django library management

Requirements:
django 4.1.3
python3
postgres 13.4

#Create postgres database running on port 5432. Tweak database settings in settings.py in section DATABASES
`
DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'library',
          'USER': 'user',
          'PASSWORD': '',
          'HOST': '127.0.0.1',
          'PORT': '5432'
      }
  }
`
Steps to create postgres database
 - run initdb -D data-lib
 - postgres -D data-lib -p 5432
 - createdb -p 5432 library
 - pg_ctl -D data-lib start
 - psql -p 5432 library
 - create user 'user' with superuser

Steps to set up the app
 - cd into the root directory of the project:library_mgmt
 - python3 manage.py makemigrations
 - python3 manage.py migrate
 
 Creating an admin user

  - python3 manage.py createsuperuser
  - input username:admin
  - input email
  - input password
 
Run the app
 - python3 manage.py runserver
 
Use the app
 - Go to http://127.0.0.1:8000 in your browser
 - Go to http://127.0.0.1:8000/admin. Login as admin.
 - Add books data. More than three to test features 
 - Logout
 - Go back to http://127.0.0.1:8000
 - Create user using signup feature. 
 - Checkout books
 - CheckIn books
 
 
 
