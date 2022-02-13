# Basique

This the base project I'm using for doing quick proof of concepts with Django.

It's provide:

- Django
- Django Q job queue
- Tailwind
- Type checking
- Basic theme
- A full featured articles models + controller for embeding a blog
- PostgreSQL
- Procfile support with honcho
- Can be deployed on Dokku or Heroku

## License

Apache 2


### Setup

Install poetry.

```
./bin/setup
```

## Migration

### Run the migration

```
python manage.py migrate
```

## Start the server

```
./bin/dev
```

## Update translations

```
django-admin makemessages -a
django-admin compilemessages
```