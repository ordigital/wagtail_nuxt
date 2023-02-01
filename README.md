# Dockerized **Wagtail 4** + **NuxtJS 3** + **Graphene 3** + **Vuetify 3**
![wagtail_nuxt banner](https://github.com/ordigital/wagtail_nuxt/blob/main/wagtail_nuxt.jpg?raw=true)
---
# **For developement:**

## 1. Clone repository
```bash
$ git clone git@github.com:ordigital/wagtail_nuxtjs.git && cd wagtail_nuxtjs
```

## 2. Build Docker images
Execute this command to build Docker images with access to local `frontend` and `backend` folders (see `docker-compose.yml`). This way live changes in code would be possible (needs at least 2GB free space):
```bash
$ ./run dev
```
## 3. Create Wagtail superuser 
Execute this command in console while docker dev images are running to be able to run `./manage.py`:
```bash
$ ./run wag
```

## 4. Test if http endpoints are working
Open Wagtail admin panel to add some subpages to `Home` with `News Page` type.
Then open frontend to test if GraphQL api is fetching data.

- **Backend admin panel: http://localhost:8000/admin** *(remember to add some NewsPages to test api!)*
- **Simple frontend with GraphQL test: http://localhost:8000**
- GraphQL console for testing: http://localhost:8000/api/graphiql
- GraphQL api: http://localhost:8000/api/graphql *(try `/api/graphql/?query articles { articles {title intro}}`)*
- Wagtail api: http://localhost:8000/api/v2/ *(try `/api/v2/pages` to test)*

You can also install [Vue.js devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd/related) and [Apollo Client Tools](https://chrome.google.com/webstore/detail/apollo-client-devtools/jdkknkkbebbapilgoeccciglkfbmbnfm) for Chrome/Brave to make your work easier.

---

# **For production**:

## 1. Run containers for production
```bash
$ ./run prod
```

## 2. Test if Nginx proxy responds
- **http://localhost:8000** should point to NuxtJS static frontend
- **http://localhost:8000/static** should point to Wagtail static folder
- **http://localhost:8000/admin** should point to Wagtail admin panel
- **http://localhost:8000/django-admin** should point to Django admin panel

## 2. Customize settings
If everything went well, stop container and edit `backend/backend/.env` to set important variables. Now you can build again and use images for production server.

## 3. Export files
Run command below to create `wagtail_nuxt_production.tar.gz` file with everything you need to deploy on server:
- Wagtail with Gunicorn Docker image (port 7999)
- Wagtail static files directory
- Wagtail database db.sqlite3
- Wagtail .env file
- Nginx public static files 
- Nginx sample proxy file.
```bash
$ ./run save
```

## 4. Deploy on server

- Use `docker load -i ./wagtail_gunicorn.tar` to import docker image.
- Create vhost config based on `nginx.conf`.
- Copy `/static` and `/public` to where nginx proxy would get them from.
- Use `docker run` with exec command `./docker-entrypoint.prod.sh` to start container from image.

### **Remember you must bind some source files because db.sqlite3 and .env is not in docker image!!!** ###

Example:
```bash
docker run -d \
     --name wagtail  \
     --mount type=bind,source=/LOCAL/db.sqlite3,target=/app/db.sqlite3 \
     --mount type=bind,source=/LOCAL/.env,target=/app/backend/.env \
     --restart=unless-stopped \
     -p 7999:7999 \
     wagtail_nuxt_web \
     ./docker-entrypoint.prod.sh
```

# Enjoy! :)
