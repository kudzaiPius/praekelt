Overview
++++++++

This is an application that handles lecturer adminstration and communications

+ **Basic admin functions**
    Handled by django default structures.

    + Available actions for current build :
		- Add Lecturer
		- Delete Lecturer
		- Edit Lecturer

+ **Communication**
   The user can utilise the message system through the `message Lecturer <http://127.0.0.1:8000/message-Lecturer/>`_ page.

+ **Lecturer Information**
   Minimal information (name, surname, full_name) is made avilable on the admin lecturer page. More detailed information is viewable on the `lecturers <http://127.0.0.1:8000/lecturers/>`_ page.


Project Structure
+++++++++++++++++

    + **Basic Structure**
        - Main project is 'praekelt'.
        - Main application is 'campus'.
        - Base directory set to location of 'praekelt/' directory.

    + **Extra enabled settings** (in *'/praekelt/settings.py'*)
        - **static file directory** : allow css styling sheets and image files.
        - **template directory** : custom forms with html and django template language.

    + **Custom structures**
        - **custom fields** : to be defined in *'campus/customfields.py'*. Reusable types that combine field types and custom validations.

        - **validators** : custom validators defined in *'campus/validators.py'*. Reusable(in different structures/different parts of code, in models themselves or in views) and allow centralized optimizations.

        - **static files** : enabled in settings, and contained in the folder *'/static/'*. contains styling and image files and folders.