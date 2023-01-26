# Dockerized **Wagtail 4** + **NuxtJS 3** + **Graphene 3** + **Vuetify 3**
![wagtail_nuxt banner](https://github.com/ordigital/wagtail_nuxt/blob/main/wagtail_nuxt.jpg?raw=true)
---
# **For developement:**

## 1. Clone repository
```bash
$ git clone git@github.com:ordigital/wagtail_nuxtjs.git
$ cd wagtail_nuxtjs
```

## 2. Build Docker images
Execute commands below to build Docker images with access to local `frontend` and `backend` folders (see `docker-compose.yml`). This way live changes in code would be possible (needs at least 2GB free space):
```bash
$ docker-compose up --build --force-recreate
```
or use ready script:
```bash
$ chmod +x ./dev
$ ./dev
```
## 3. Open frontend
If there were no errors you should be able to open **http://localhost:8000** and see example NuxtJS page made using Vuetify with GraphQL for fetching test.

**Web endpoints:**
- Frontend: http://localhost:8000
- Backend admin panel: http://localhost:7999/admin *(remember to add some NewsPages to test api!)*
- GraphQL console for testing: http://localhost:7999/api/graphiql
- GraphQL api: http://localhost:7999/api/graphql *(try `/api/graphql/?query articles { articles {title intro}}`)*
- Wagtail api: http://localhost:7999/api/v2/ *(try `/api/v2/pages` to test)*

## 4. Create Wagtail superuser 
You can access backend Docker image to create superuser using `manage.py`:
```bash
$ docker ps # find ID of backend image
$ docker exec -it BACKEND_IMAGE_ID bash
$ ./manage.py createsuperuser 
```

## 5. Add some articles
Open **http://localhost:7999/admin** and add some articles as subpages of Home with `News Page` model.

## 6. Test fetching in frontend
Open **http://localhost:8000** again, click `re-fetch` button (or refresh page) and see if page titles are visible in sidebar menu. After clicking on title, full content should appear in main window.

## 7. Customize everything you want
Now you can develop your application. Take a look at all config files to see what is going on.
Also **remember to change SECRET_KEY in `backend/backend/settings/base.py` before deploying!**.
You can generate new secret key using command from backend Docker image:
```bash
$ ./manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
You can also install [Vue.js devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd/related) and [Apollo Client Tools](https://chrome.google.com/webstore/detail/apollo-client-devtools/jdkknkkbebbapilgoeccciglkfbmbnfm) for Chrome/Brave to make your work easier.

---

# **Deploying for production**:

## 1. Set `.env` file and test settings
Go to `backend/` and rename `sample.env` to `.env`, edit it and change settings you want including `SECRET_KEY`:
```bash
$ mv ./sample.env ./.env
$ nano ./.env # or vim, mcedit, code etc.
```
Do not set up SSL redirect until you test that everything will work without it.

## 2. Generate static files for NuxtJS
Config file `nuxt.config.ts` has setting for `httpEndpoint` both for developement (API on port 7999) and production (API on port 8000).
```bash
$ chmod +x ./nuxt
$ ./nuxt
```

## 2. Run containers for production
```bash
$ chmod +x ./prod
$ ./prod
```

## 3. Test if Nginx proxy responds
- **http://localhost:8000** should point to NuxtJS static frontend
- **http://localhost:8000/static** should point to Wagtail static folder
- **http://localhost:8000/admin** should point to Wagtail admin panel
- **http://localhost:8000/django-admin** should point to Django admin panel

## 4. Do whatever you like
Now you can save container and run it on a production server with port forwarding.
