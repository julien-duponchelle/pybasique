# Basique

This the base project I'm using for doing quick proof of concepts with Django.

It's provide:

- Django
- Tailwind
- Type checking
- A full featured articles models + controller for embeding a blog
- PostgreSQL
- Procfile support with honcho
- Can be deployed on Dokku or Heroku

## License

Apache 2

## Setup

```
cp env.sample .env
```

### PostgreSQL

```
sudo -u postgres createuser --interactive -d

# Set password
sudo -u postgres psql
postgres=# \password pybasique
```

### Run setup

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
