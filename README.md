# Django Blog 🌸

## Set up instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/sofijasljusar/django-blog.git
   cd django-blog
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file**

   Create a file named `.env` in the root directory and add the following variables:

   ```
   SECRET_KEY=your_secret_key
   DEBUG=False
   ```

5. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create superuser**

   ```bash
    python manage.py createsuperuser
   ```
   
8. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
   
   Access the admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
