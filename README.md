# Marekberry Picam

https://github.com/user-attachments/assets/7aed0a54-8252-4912-9373-3a65db7da313

## Requirements

```
sudo apt-get install python-picamera python3-picamera
```

Also `picamera` needs to be installed. Didn't work on macosx...


To migrate models to the database (after changes):

```
python manage.py makemigrations
python manage.py migrate
```

## Run the django project

```
python manage.py runserver 0.0.0.0:8000
```


