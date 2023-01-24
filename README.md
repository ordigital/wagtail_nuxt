# Backend: **Wagtail** 4.1.1 + Frontend: **NuxtJS** 2.15.8 + API: **graphene-django** 3.0.0


## Download repository:
```bash
$ git clone git@github.com:ordigital/wagtail_nuxtjs.git
$ cd wagtail_nuxtjs
```

## How to use:
Commands below allow you to build Docker images with access to local `frontend` and `backend` folders (see `docker-compose.yml`). This way changes would be applied on save.
```bash
$ docker-compose build
$ docker-compose up
```

You can access backend Docker image to create superuser:
```bash
$ docker ps # find ID of backend image
$ docker exec -it BACKEND_IMAGE_ID bash
$ ./manage.py createsuperuser 
```

**If there was no error you should be able to access links:**
- Frontend: http://localhost:8000
- Backend admin panel: http://localhost:7999/admin *(remember to add some NewsPages to test api!)*
- GraphQL console for testing: http://localhost:7999/api/graphiql
- GraphQL api: http://localhost:7999/api/graphql *(try `/api/graphql/?query articles { articles {title intro}}`)*
- Wagtail api: http://localhost:7999/api/v2/ *(try `/api/v2/pages` to test)*

**Remember to change SECRET_KEY in `backend/backend/settings/base.py` before deploying!**
You can generate new key by command:
```bash
$ ./manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Tips:
- first take a closer look at `docker-compose.yml` in root directory, `Dockerfile` in `frontend` and `backend` dir, and 'docker-entrypoint.sh` in `backend` dir to understand what is happening
- default app is in `backend/app` folder
- GraphQL schema is in `backend/app/schema.py` and is connected to `models.py`

## Deploying for production:
*[ soon… ]*

## Run Wagtail without Docker
```bash
$ python -m env
$ source env/bin/activate
$ pip install -r ./requirements.txt
$ cd backend
$ ./manage.py migrate  # Update database
$ ./manage.py createsuperuser # Create admin user
$ ./manage.py runserver # Run Wigtail web server
```
## Run NuxtJS without Docker
First pdate npm version:
```bash
$ sudo npm cache clean -f # Prepare npm
$ sudo npm update npm -g # Update npm
$ sudo n stable # Install stable version of npm
```
Now install dependencies and serve frontend:
```bash
$ cd frontend
$ npm install
$ npm run dev # use "npm run generate" to generate static files
```