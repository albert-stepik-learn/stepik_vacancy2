# Stepik Vacancies: Project 4

This is a part of my learning at https://stepik.org/course/63298.

The Django application presented here shows three types of pages:

- ``main`` shows a list of vacancy specialities and companies supplying vacancies
- ``companies`` and ``company`` present company related vacancy data
-  ``speciality`` and ``specialities`` present groups of vacancies

## Prerequisites

The application requires Python 3.7 or a newer version.

## Installation

To use this application, go through the following steps:

1. Download this repository and unpack it. This will create the ``stepik_vacancy1-main`` directory.
0. Go in this directory:

    ```bazaar
    cd stepik_vacancy1-main
    ```

0. Create a Python virtual environment:

    ```bazaar
    python3 -m venv venv
    ```
   
0. Activate the virtual environment:

    ```bazaar
    source venv/bin/activate
    ```
   
0. Install the required Python packages:

    ```bazaar
    pip install -r requirements.txt
    ```
   
0. Run the application:

    ```bazaar
    python manage runserver
    ```
   
0. Address your browser to the following URLs:

    -   http://localhost:8000/
    -   http://localhost:8000/vacancies/
    -   http://localhost:8000/vacancies/2/
    -   http://localhost:8000/companies/
    -   http://localhost:8000/companies/1/
    -   http://localhost:8000/vacancies/cat/backend/
 
## Some Tips when Developing the Project

### DB Client

To watch a database content, I used the DBeaver client. On Mac, install it as follows:

```
    % brew install --cask dbeaver-community
```

### Using Static Content

1. Put all your static files to the ``<application>/static/<application>/`` folder. In this project, \<application\>
   is "vacancy".
1. On top of the template, where you want to use static files, add just after ``{% extends... %}``:

   ```bazaar
   {% load static %}
   ```

1. In the place of the template, where you want to use a static file, use the ``static`` tag as in the following
   example:

   ```bazaar   
   <img class="mx-auto d-block mw-100" src="{% static 'vacancy/'|add:company.logo %}" alt="">
   ```
   
### Counting related Objects

If you need to count related objects (one-to-many relationship), for example, a number of vacancies exposed
by a company, use the ``related_name`` property as in the following example (related name is 'vacancies'):

1. In the model class definition, add the ``related_name`` parameter to the foreign key that you are going to use:

   ```bazaar   
   company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
   ```
   
1. In a template, use this property as in the following example that counts the number of vacancies published by a company:
 
    ```bazaar
     <p class="card-text"><a href="#">{{ company.vacancies.count }} вакансий</a></p>
    ```

That's it. See you in the next project.

