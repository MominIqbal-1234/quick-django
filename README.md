# quick-django

Create django project quickly single command with all necessary file like djnago app, urls.py, templates folder, static folder and add the default code in view.py,models.py,admin.py and create index.html

# How to use quick-django
### Step: 1
```python
pip install quick-django
```
### Step: 2
### Window
open cmd in your porject folder and run this command
        
```python
python -m quick-django myproject myproject_app 
```

### Linux
open terminal in your porject folder and run this command
        
```python
python3 -m quick-django myproject myproject_app 
```

### Configuration
```python
# setting.py
 INSTALLED_APPS = [
            ....
       'myproject_app',
       
        ]

```

# For Rest-Api

### Window
open cmd in your porject folder and run this command
        
```python
python -m quick-django myproject myproject_app --restapi
```

### Linux
open terminal in your porject folder and run this command
        
```python
python3 -m quick-django myproject myproject_app --restapi
```

### Configuration
```python
# setting.py
 INSTALLED_APPS = [
            ....
       'myproject_app',
       'rest_framework'
       
        ]

```


Check Our Site : https://mefiz.com </br>
pypi site : https://pypi.org/project/quick-django/

