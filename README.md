# 🚀 The Ultimate Django Series: Part 1

## 📚 What I've Learned So Far

- ✅ Setting up development environment
- ✅ Creating Django Project
- ✅ Mapping URLs to Views
- ✅ Debugging within Django
- ✅ Building Data Models

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

## 📝 Next Steps

- [ ] Learn about Django models and database migrations
- [ ] Django ORM
- [ ] Admin Site

---


*Happy coding! 🎉*
