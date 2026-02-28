# Online Course Management System (OCMS)

This repository contains a Django-based web application for managing online courses. The project provides functionality for user registration, course enrollment, content management, reviews, and dashboards for administrators and students.

## Features

- User authentication and profiles
- Course listing and detail pages
- Enrollment workflows
- Review system for courses
- Dashboard overview for users and admins
- REST API endpoints using Django REST Framework
- Responsive frontend with basic HTML/CSS/JavaScript

## Project Structure

```
ocms/               # Django project
    accounts/        # User accounts app
    courses/         # Course management app
    enrollments/     # Enrollment handling
    reviews/         # Course reviews
    dashboard/       # Dashboard views
    static/          # Static files (CSS, JS)
    templates/       # HTML templates
```

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/ReethikReddy/Online-Course-Management-System.git
   cd Online-Course-Management-System
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   env\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser at `http://127.0.0.1:8000/`

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with relevant changes. Be sure to run tests and follow code style guidelines.

## License

This project is open source and available under the MIT License.

## Contact

For questions or support, open an issue on GitHub or contact the maintainer.
