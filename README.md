# Secure Password Manager

This is a secure password management application built with Python and Flask. It allows users to store, retrieve, and generate strong passwords for their various accounts.

## Features

- Secure storage of passwords using encryption
- Generate strong, random passwords
- View stored passwords
- Add new password entries
- Simple and intuitive web interface

## Security

This application uses Fernet symmetric encryption to secure stored passwords. Each user's passwords are encrypted with a unique key, ensuring that even if the database is compromised, the passwords remain protected.

## Usage

1. Add new passwords by providing an account name and password
2. Use the "Generate Password" feature to create strong, random passwords
3. View all stored passwords in a secure environment

## Technical Details

- Backend: Python with Flask framework
- Database: SQLite with SQLAlchemy ORM
- Encryption: Fernet (from the cryptography library)
- Frontend: HTML, CSS, and JavaScript

## Setup

1. Clone the repository
2. Install required dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the web interface at `http://localhost:5000`

## Note

This project is for educational purposes. While it implements basic security measures, it's recommended to use well-established password managers for critical personal or business use.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.

## License

[MIT](saharshbaweja 2024)
