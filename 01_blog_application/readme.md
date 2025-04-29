# 📝 **Blog Website Project Guide**

Welcome to the **Blog Website Project**! 🚀 This project is a fully-featured blog application built with Django, designed to help you learn and master web development concepts. Below, you'll find a detailed guide to set up, configure, and use the project effectively.

---

## ✨ Project Demo

Below is a quick demo of how the blog website looks and works:
<div align="center">
<img src="./assests/demo.gif"/>
</div>

## ✨ Features

### 🛠️ Building a Blog Application

- Learn the basics of Django by developing:
  - **Models** for blog posts and related data.
  - **Views** to handle requests and render templates.
  - **Templates** for a user-friendly UI.
  - **URLs** to map routes to views.
- Gain hands-on experience with the **Django ORM** to create QuerySets.
- Configure the **admin interface** for easy content management.


- Add advanced functionality to your blog:
  - **Pagination** for better navigation through posts.
  - **Email integration** for notifications (e.g., contact forms).
  - **Form handling** for user inputs (e.g., comments).
- Improve user engagement with a **comment system** to allow feedback on posts.
  - Integrate **django-taggit** for tagging posts.
  - Build complex QuerySets to suggest **related posts**.
  - Create **custom template tags and filters** for enhanced template functionality.
- Add a **sitemap** for better SEO.
- Enable robust **full-text search** using PostgreSQL.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- 🐳 **Docker** and **Docker Compose** (to run the application in containers).
- 🐍 **Python 3.12** (if you need to install dependencies manually).
- 🗄️ **PostgreSQL** (used as the database; managed via Docker in this setup).
- 📧 A **Gmail account** for email integration (for sending notifications).

---

## 🛠️ Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone  https://github.com/HashimThePassionate/Django-Projects-Hub.git 
cd Django-Projects-Hub/01_blog_application
```

### 2. Configure Environment Variables

The project uses environment variables for sensitive settings (e.g., email credentials, database settings). These are defined in the `docker-compose.yml` file but should be updated with your own values:

- Open the `docker-compose.yml` file.
- Update the following environment variables under the `web` service:
  - `EMAIL_HOST_USER`: Your Gmail address (e.g., `your_account@gmail.com`).
  - `EMAIL_HOST_PASSWORD`: Your Gmail app password (not your regular password; generate one from Gmail's security settings).
  - `DEFAULT_FROM_EMAIL`: The email address to use as the sender (e.g., `My Blog <your_account@gmail.com>`).

Example:

```yaml
environment:
  EMAIL_HOST_USER: 'your_account@gmail.com'
  EMAIL_HOST_PASSWORD: 'your-app-password'
  DEFAULT_FROM_EMAIL: 'My Blog <your_account@gmail.com>'
  DB_HOST: 'db'
  DB_USER: 'postgres'
  DB_PASSWORD: 'postgres'
  DB_NAME: 'postgres'
```

### 3. Build and Run the Application with Docker

The project uses Docker to manage services (web app and database). Follow these steps:

1. Build the Docker images:

   ```bash
   docker-compose build
   ```
2. Start the containers:

   ```bash
   docker-compose up -d
   ```
   - This will start the following services:
     - `web_run`: The Django development server running on `http://localhost:8000`.
     - `web_migrate`: Applies database migrations.
     - `db`: A PostgreSQL database.

### 4. Access the Application

- Open your browser and go to:

  ```
  http://localhost:8000
  ```
- The blog website should now be running! 🌐

### 5. Access the Admin Interface

- Create a superuser to access the Django admin interface:

  ```bash
  docker-compose exec web_run python /code/mysite/manage.py createsuperuser
  ```
- Follow the prompts to set up a username, email, and password.
- Visit `http://localhost:8000/admin` and log in with your superuser credentials.

---

## 📖 Usage

Here’s how to use the blog application and explore its features:

### 1. Create and Manage Blog Posts

- Log in to the admin interface (`http://localhost:8000/admin`).
- Navigate to the "Blog" section and add new posts.
- Add tags to your posts for better categorization.

### 2. Explore the Blog

- Visit the homepage (`http://localhost:8000`) to see the list of published posts.
- Use the **pagination** links to navigate through multiple pages of posts.
- Click on a post to view its details, including tags and related posts.

### 3. Engage with Comments

- On a post’s detail page, users can leave comments.
- Comments are displayed below the post content.

### 4. Search for Posts

- Use the search bar in the sidebar to perform a full-text search.
- Search results will display posts containing your query in the title or body.

### 5. Subscribe via RSS Feed

- Access the RSS feed at `http://localhost:8000/feed/` to subscribe to blog updates.

### 6. Check the Sitemap

- View the sitemap at `http://localhost:8000/sitemap.xml` for SEO purposes.

---

## 🗂️ Project Structure

Here’s a quick overview of the key files and directories:

- `Dockerfile`: Defines the Docker image for the Django application.
- `docker-compose.yml`: Configures the services (web app, migrations, and database).
- `requirements.txt`: Lists Python dependencies for the project.
- `settings.py`: Django settings file with configurations for apps, database, email, and more.
- `blog/`: The main Django app containing models, views, templates, and other logic.

---

## 🛠️ Dependencies

The project uses the following Python packages (as listed in `requirements.txt`):

- `asgiref==3.8.11`
- `Django==5.2`
- `django-bootstrap4==24.4`
- `django-crispy-forms==2.3`
- `django-taggit==5.0.1`
- `Markdown==3.6`
- `psycopg-binary==3.1.18`
- `python-decouple==3.8`
- `sqlparse==0.5.3`

These are automatically installed when you build the Docker image.

---

## ⚙️ Configuration Details

### Database

- The project uses **PostgreSQL** as the database, managed via Docker.
- Database settings are configured in `settings.py` and sourced from environment variables in `docker-compose.yml`.

### Email Integration

- Email notifications are sent via Gmail’s SMTP server.
- Ensure you have set the correct `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, and `DEFAULT_FROM_EMAIL` in `docker-compose.yml`.

### Static Files

- Static files (CSS, JavaScript, images) are served from the `static/` directory.
- The project uses Google Fonts (`Inter`) for typography.

---

## 🚀 Tips for Development

- **Debug Mode**: The project runs with `DEBUG = True` for development. Disable this in production for security.
- **Custom Template Tags**: Check the `blog/templatetags/` directory for custom tags and filters.
- **Full-Text Search**: Ensure PostgreSQL is properly configured for full-text search functionality.
- **Logs**: View container logs with:

  ```bash
  docker-compose logs
  ```
