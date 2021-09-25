This is a test repo for experimenting with django_huey. It isn't meant to be a guide for best practices or anything like that - I'm also trying to make sure I understand how not do things.

## Notes


```bash
# bringing up 
docker-compose up -d

# starting a queue
docker-compose exec web bash
poetry shell
cd django_huey_test
python manage.py djangohuey

# separate panel
python manage.py djangohuey --queue process
```