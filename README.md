# Verve - A Social Media App

Verve is a dynamic and interactive social media application designed to connect people, share ideas, and foster a vibrant online community. Built with cutting-edge web technologies, Verve aims to deliver a seamless user experience while prioritizing privacy and performance.

---

## Features

- **User Registration**: Secure registration system for new users.
- **User Login**: Authentication system for secure access.
- **Password Recovery**: Recover passwords through registered email via OTP verification.
- **Post Interaction**: Users can see posts from other users, like posts, and add comments.
- **My Posts Section**: A dedicated section for logged-in users to view and manage their own posts.

---

## Tech Stack

### Frontend:
- HTML
- CSS
- JavaScript

### Backend:
- Django

### Database:
- MySQL

### Communication:
- Fetch API (for data transfer between frontend and backend)

---

## Installation

Follow these steps to set up the project locally:

### Prerequisites:
- Python 3.x
- MySQL

### Clone the Repository:
```bash
$ git clone https://github.com/praneeth552/verve.git
$ cd verve
```

### Backend Setup:
```bash
$ cd backend
$ python -m venv env
$ source env/bin/activate  # On Windows, use `env\Scripts\activate`
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### Frontend Setup:
Simply run the Django server and navigate to the application URL in your browser.

---

## Project Structure

```
verve/
|
|-- backend/          # Django backend
|   |-- manage.py     # Django project management script
|   |-- verve/        # Main Django project folder
|       |-- settings.py  # Project settings
|       |-- urls.py      # URL configuration
|       |-- wsgi.py      # WSGI application
|   |-- app/          # Django app folder
|       |-- models.py     # Database models
|       |-- views.py      # View logic
|       |-- templates/    # HTML templates (frontend files)
|           |-- index.html  # Main HTML file
|           |-- other_html_files.html  # Other HTML files
|       |-- static/       # Static files (CSS, JS)
|           |-- css/         # CSS folder
|               |-- styles.css  # CSS styles
|           |-- js/          # JavaScript folder
|               |-- app.js    # JavaScript logic
|
|-- README.md         # Project documentation
```

---

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add your feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

---

## Screenshots

### User Registration
<img width="1470" alt="Screenshot 2024-12-24 at 15 31 57" src="https://github.com/user-attachments/assets/b928d65e-dc1f-4dc2-b9b2-678ed1c2fb24" />

### User Login
<img width="1470" alt="Screenshot 2024-12-24 at 15 31 48" src="https://github.com/user-attachments/assets/a9fa1e57-d8ca-4248-a814-23475a5ded99" />

### Home Page
<img width="1470" alt="Screenshot 2024-12-24 at 15 31 34" src="https://github.com/user-attachments/assets/da3f6094-d5ac-4805-8fa3-d0f14dcdeb4f" />

### Password Recovery Through OTP Verification
<img width="1470" alt="Screenshot 2024-12-24 at 15 32 32" src="https://github.com/user-attachments/assets/a36d18f7-c866-47ac-8b61-9146b0f283a6" />

---

## Acknowledgments

- Inspiration from popular social media platforms.

---

## Contact

- **Author**: KOTYADA SAI PRANEETH
- **Email**: saipraneeth2525@gmail.com
- **GitHub**: [praneeth552](https://github.com/praneeth552)

Feel free to open issues or pull requests for suggestions or bug fixes!

