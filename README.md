# ChaiHQ: Social Pulse

ChaiHQ: Social Pulse is a robust Django-based web application designed for sharing thoughts, moments, and media. With a focus on simplicity and user experience, it enables users to post, view, and manage tweets, including photo uploads, all within a modern and responsive interface.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Post, edit, and delete tweets
- Upload and display photos with tweets
- Clean, responsive UI with custom templates
- Django admin for easy content management
- Secure media handling
- Modular and scalable codebase

## Project Structure

```
chaiheadq/
├── chaiheadq/           # Project settings and configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tweet/               # Tweet app: models, views, forms, templates
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   │   └── index.html
│   └── ...
├── media/               # Uploaded photos
│   └── photos/
├── templates/           # Base templates
│   └── layout.html
├── static/              # Static files (CSS, JS, images)
├── db.sqlite3           # SQLite database
└── manage.py            # Django management script
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/kushal15-neub/ChaiHQ-Social-Pulse.git
   cd ChaiHQ-Social-Pulse
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   .\\venv\\Scripts\\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the app at `http://127.0.0.1:8000/`
- Log in to the Django admin at `http://127.0.0.1:8000/admin/` to manage tweets and users
- Upload photos with your tweets for richer content

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, please contact [kushal15-neub](https://github.com/kushal15-neub).
