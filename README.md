# Blog App (THOUGHTFLOW)

A blog application built with Django. This application allows users to create, view, and comment on blog posts.

## Features

- User authentication
- Create and manage blog posts
- Comment on blog posts
- View similar posts based on category
- Search and list posts
- Manage and update user profile

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Manalhub/THOUGHTFLOW.git
   cd THOUGHTFLOW_blog
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply the migrations:**

   ```bash
   python manage.py migrate
   ```


5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage
Watch the demo video below:

[![Watch the video](https://img.youtube.com/vi/https://www.youtube.com/watch?v=hBL_1A5ju0o/maxresdefault.jpg)](https://www.youtube.com/watch?v=hBL_1A5ju0o)

## Testing

To run the tests, use the following command:

```bash
python manage.py test
```

The tests are located in the `tests.py` file within each app directory. 

## Project Structure

```
THOUGHTFLOW_blog/
├── base/
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── profiles/
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── THOUGHTFLOW_blog/
│ ├── __init__.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── static/
├── images/
├── manage.py
├── requirements.txt

```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

---

Happy coding!
```

