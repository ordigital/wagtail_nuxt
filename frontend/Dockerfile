FROM node:18.13.0-alpine

# create destination directory
RUN mkdir -p /usr/src/nuxt-app && chown -R node:node /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app

# update and install dependency
RUN apk update && apk upgrade
#RUN apk add git

# copy the app, note .dockerignore
COPY --chown=node:node . /usr/src/nuxt-app/

# fix import vuetify sass error
# RUN mkdir -p /usr/src/nuxt-app/.nuxt/
# RUN touch /usr/src/nuxt-app/.nuxt/css.mjs

# set permissions for node
# RUN chmod -R +w /usr/src/nuxt-app/node_modules/
# RUN chown -R node:node /usr/src/nuxt-app/node_modules/


#RUN npm install

# build necessary, even if no static files are needed,
# since it builds the server as well
#RUN npm run build

# expose 8000 on container
EXPOSE 8000

# set app serving to permissive / assigned
ENV NUXT_HOST=0.0.0.0
# set app port
ENV NUXT_PORT=8000
# workaround for errors
#ENV NODE_OPTIONS=--openssl-legacy-provider

# set node user
USER node



# start the app
#CMD [ "npm", "run", "dev" ]
