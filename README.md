# 🚀 The Ultimate Django Series: Part 1

## 📚 What I've Learned So Far

- ✅ Setting up development environment
- ✅ Creating Django Project
- ✅ Mapping URLs to Views
- ✅ Debugging within Django
- ✅ Building Data Models
- ✅ Django models and database migrations
- ✅ Django ORM
- ✅ Admin Site

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

### Getting Single Objects
```python
# Get object by primary key
[model].objects.get(pk=1)
```

### To find more
There are a lot of ways to filter queries
https://docs.djangoproject.com/en/5.2/ref/models/querysets/
Google Django Query Set API to find documentation


### Basic Filtering

```python
# Filter records
[model].objects.filter(pk=0)

# Check if records exist (returns boolean)
[model].objects.filter(pk=0).exists()
```

## Filtering

### String Filtering

Excercise
How do you filter customer emails that contain .com?

```python
# Filter emails containing '.com' (case insensitive)
customers = Customer.objects.filter(email__icontains='.com')
```

### AND Conditions
```python
# Multiple conditions (AND)
customers = Customer.objects.filter(
    email__icontains='.com', 
    email__icontains='somethingElse'
)
```

### OR Conditions
```python
# Import Q objects for OR conditions
from django.db.models import Q

# OR condition example
customers = Customer.objects.filter(
    Q(inventory__lt=10) | Q(unit_price__lt=20)
)
```

### Useful Resources
- [Django QuerySet API Documentation](https://docs.djangoproject.com/en/5.2/ref/models/querysets/)

## Sorting and Limiting

### Sorting
```python
# Order by column name
queryset.order_by('column_name')
```

### Limiting Results
```python
# Get first 5 objects using Python slicing
queryset.all()[:5]
```

### Selecting Specific Columns
```python
# Return only specific columns
objects.values('title', 'name')
```

## Aggregation and Annotation

### Aggregation Functions
```python
# Count total products
Product.objects.aggregate(Count('id'))
```

### Annotation
The `annotate()` method adds additional attributes to objects when querying them.

### Database Functions
```python
# Create computed field using Func()
.annotate(
    full_name=Func(
        F('first_name'), 
        Value(' '), 
        F('last_name')
    )
)
```

**Resource:** Search "Django database functions" for more available functions.

## Database Operations

### Inserting Data
```python
# Create new object
collection = Collection()
# Set attributes...
collection.save()
```

### Updating Objects
```python
# Method 1: Get and save (prevents data loss)
collection = Collection.objects.get(pk=1)
# Update attributes...
collection.save()

# Method 2: Bulk update
Collection.objects.filter(pk=11).update(column_name=new_value)
```

### Deleting Objects
```python
# Select then delete
object = Model.objects.get(pk=1)
object.delete()
```

## Transactions

Transactions maintain data integrity. If an exception occurs, all queries are rolled back.

```python
from django.db import transaction

@transaction.atomic
def example(request):
    # Your code here...
```

## Raw SQL

```python
# Execute raw SQL queries
queryset = Product.objects.raw('SELECT * FROM store_product')
```

## Django Admin

### Creating Superuser
```bash
python manage.py createsuperuser
```
Enter username, email address, and password when prompted.

### Registering Models

#### Basic Registration
```python
# In admin.py
admin.site.register(models.ModelName)
```

#### Advanced Registration
```python
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
```

**Resource:** [Django Admin Documentation](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)

## Admin Customization

### Computed Columns
```python
@admin.display(ordering='inventory')
def inventory_status(self, product):
    if product.inventory < 10:
        return 'Low'
    else:
        return 'OK'

# Add to list_display
list_display = ['title', 'unit_price', 'inventory_status']
```

### Loading Related Objects
```python
# Prevent extra queries with eager loading
list_select_related = ['relation_name']
```

### Custom QuerySet
```python
def get_queryset(self, request):
    return super().get_queryset(request)  # Override this
```

### Adding Links to Other Pages
```python
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

def custom_link(self, collection):
    url = (reverse('admin:store_product_changelist') +
           '?' +
           urlencode({
               'collection__id': str(collection.id)
           }))
    return format_html('<a href="{}">{}</a>', url, collection.products_count)
```

### Search Functionality
```python
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['column_name__istartswith']  # 'i' = case insensitive
```

### Filtering
```python
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['column_name']
```

## Custom Actions

```python
class ProductAdmin(admin.ModelAdmin):
    actions = ['custom_action_name']

    def custom_action_name(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        
        # Send message to user
        self.message_user(
            request, 
            f'{updated_count} products were updated.'
        )
```

## Form Customization

### Field Customization
```python
class ProductAdmin(admin.ModelAdmin):
    # Include specific fields
    fields = ['field1', 'field2']
    
    # Exclude specific fields
    exclude = ['field3', 'field4']
    
    # Add autocomplete
    autocomplete_fields = ['foreign_key_field']
```

**Resource:** Search "Django ModelAdmin - ModelAdmin options" for more customization options.

## Data Validation

For data validation, import validators from Django:

```python
from django.core.validators import *
```

**Resource:** Search "Django core validators" for available validation options.

## Advanced Topics to Review

- `select_related` & `prefetch_related` - For optimizing database queries
- Custom Managers - For reusable query logic

## Quick Reference

| Operation | Syntax |
|-----------|---------|
| Get single object | `Model.objects.get(pk=1)` |
| Filter records | `Model.objects.filter(field=value)` |
| Check existence | `Model.objects.filter().exists()` |
| Case insensitive search | `field__icontains='value'` |
| OR conditions | `Q(condition1) \| Q(condition2)` |
| Ordering | `.order_by('field')` |
| Limiting | `.all()[:5]` |
| Count | `.aggregate(Count('field'))` |

---



