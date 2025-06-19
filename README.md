#  Vocal Pad

1. *Vocal Pad* is a Django-based web application designed to handle and manage audio or vocal-related content in a structured way.
2. It  allows users to register, log in, and create notes using their voice. The spoken input is converted into text, which can then be saved as a PDF for future reference. Users can also upload these PDFs later and listen to the content through text-to-speech functionality. The platform offers a simple and efficient way to manage voice-generated notes in both written and audio formats.   
3. It demonstrates clean use of Django’s MVC pattern with organized static files, media file handling, and a modular app structure.



##  Features

- Built using Django framework
- Organized project structure with app-level separation
- Static files handling (CSS, JS, Images)
- Media folder support for file uploads
- Template integration with dynamic content rendering



##  Technologies Used

- Python
- Django
- HTML5 / CSS3
- JavaScript
- Bootstrap (if used)

##  Project Structure Overview

```bash
vocal_pad/
├── vocal_app/
│   ├── templates/
│   ├── static/
│   └── views.py, models.py, urls.py, etc.
├── media/
├── db.sqlite3
├── manage.py 
```


## How To Run

1. Clone the repo and open the folder:
   ```bash
   git clone https://github.com/Khushi-Mishra-dev/vocal-pad.git
   cd vocal-pad
   
2. Create & Activate Virtual Environment:
    ```bash
    python -m venv env
    env\Scripts\activate

3. Run migrations and start Server:
    ```bash
    python manage.py migrate
    python manage.py runserver

 Open browser at 
   http://127.0.0.1:8000/

 
##  Author

**Khushi Mishra**  
[GitHub Profile](https://github.com/Khushi-Mishra-dev)
