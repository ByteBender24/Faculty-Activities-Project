
# Faculty Activities Project

This project is aimed at managing various activities related to faculty members in an academic institution. It provides functionalities for managing admin logins, faculty logins, recording staff development program (SDP) attendance, organizing SDP events, and more.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ByteBender24/Faculty-Activities-Project.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Faculty-Activities-Project
   ```

3. **Set up a virtual environment:**
   ```bash
   python -m venv env
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

   - On Bash:
     ```bash
     source env/bin/activate
     ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   Open a web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- **Admin Login:** Navigate to the admin login page and log in with admin credentials to access administrative functionalities.
- **Faculty Login:** Faculty members can log in to access their respective features and activities.
- **Recording SDP Attendance:** Admin users can record attendance for staff development program events, specifying details like staff attended, event type, duration, etc.
- **Organizing SDP Events:** Admin users can organize and manage staff development program events, specifying details like event name, duration, participants, resource persons, etc.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

