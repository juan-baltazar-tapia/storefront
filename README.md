# 🚀 The Ultimate Django Series: Part 1

## 📚 What I've Learned So Far

- ✅ Setting up development environment
- ✅ Creating Django Project
- ✅ Mapping URLs to Views
- ✅ Debugging within Django
- ✅ Building Data Models
- ✅ Django models and database migrations

---

## 🛠️ Getting Started

### Prerequisites
1. **Install Python** - Download from [python.org](https://python.org)
2. **Install pipenv**
   ```bash
   $ brew install pipenv
   # OR
   $ pip3 install pipenv
   ```

### Project Setup
1. **Create project directory**
   ```bash
   $ mkdir storefront
   $ cd storefront
   ```

2. **Install Django**
   ```bash
   $ pipenv install Django
   ```

3. **Activate virtual environment**
   ```bash
   $ pipenv shell
   ```

4. **Start new Django project**
   ```bash
   $ django-admin startproject [name of project] .
   ```

5. **Run the development server**
   ```bash
   $ python manage.py runserver
   ```

---

## 💻 VSCode Setup

### Configuring Python Interpreter
1. **Get virtual environment path**
   ```bash
   $ pipenv --venv
   ```

2. **Copy the path**

3. **Set interpreter in VSCode**
   - Press `CMD + SHIFT + P` (macOS) or `CTRL + SHIFT + P` (Windows/Linux)
   - Search for "Python Interpreter"
   - Click "Enter interpreter path..."
   - Paste virtual environment path and append `/bin/python`

4. **Open integrated terminal**
   - Go to **View** → **Terminal**

---

## 🔧 Creating New Apps

```bash
$ python manage.py startapp [app_name]
```

> **Important:** Remember to add your new app to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'your_app_name',  # Add your app here
]
```

---

## 🐛 Debugging in Django

### Setup Debugging in VSCode
1. **Open Run and Debug panel** (left sidebar)
2. **Create launch configuration**
   - Click "create a launch.json file"
   - Select "Django" option
3. **Set breakpoints** by clicking left margin of code lines
4. **Start debugging** with F5

### Debug Controls
- **Step Over**  - Execute current line and move to next
- **Step Into**  - Enter function calls to debug line by line
- **Continue**  - Run until next breakpoint

---

## ⚠️ Common Issues & Solutions

### SyntaxError: invalid syntax
**Fix:** Open a new terminal window and try again

### Virtual Environment Issues
- Make sure you're in the correct directory
- Verify pipenv is properly installed
- Try `pipenv --venv` to check if virtual environment exists

---
# Django Database Relationships & ORM Guide

## Defining Relationships

### One-to-One Relationship
Define within the class:
```python
customer = models.OneToOneField(
    [parent_entity], 
    on_delete=[set_property]
)
```

### One-to-Many Relationship
Define within the child entity class:
```python
customer = models.ForeignKey(
    [parent_entity], 
    on_delete=[set_property]
)
```

## Database Migrations

### Setting Up Migrations
Create migration files:
```bash
python manage.py makemigrations
```

### Running Migrations
Apply migrations to database:
```bash
python manage.py migrate
```

### Undoing Migrations
Revert to a specific migration:
```bash
python manage.py migrate [app_name] [migration_number]
```
*Note: This reverts up to (but not including) the migration you want to undo*

```bash
# View commit history
git log --oneline

# Reset to previous commit
git reset --hard HEAD~1
```

## Database Connection

### Connecting with DataGrip (MySQL)
1. Create new file in DataGrip
2. Add database using Query Console
3. Install MySQL client:
   ```bash
   pipenv install mysqlclient
   ```

## Django ORM Overview

### What is ORM?
Data is stored in rows and tables. To retrieve that data, you traditionally had to:
1. Create a SQL query
2. Send it to the database
3. Read the result
4. Map it into an object

**ORMs solve this problem** by providing an abstraction layer.

### How Django ORM Works
- Every model has a attribute called objects, which returns a manager, which is an interface to the db
The manager has a bunch of methods for queuing and updating data. Most methods return a query set


## 📝 Next Steps

- [ ] Django ORM
- [ ] Admin Site





