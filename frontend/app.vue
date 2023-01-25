<template>
  <div>
  <v-app id="wagtail_nuxt">

    <!-- DRAWER -->
    <v-navigation-drawer v-model="drawer">
      
      <!-- list pages -->
      <v-list v-if="data?.articles">
        <v-list-subheader>NEWS ARTICLES IN DATABASE</v-list-subheader>

          <!-- iterate -->
          <v-list-item
            v-for="(item, i) in data.articles"
            :key="i"
            :value="item"
            active-color="primary"
            rounded="xl"
          >
            <!-- add icon -->
            <template v-slot:prepend>
              <v-icon :icon="item.icon"></v-icon>
            </template>

            <!-- display title-->
            <v-list-item-title v-text="item.title" @click="getPost(item)"></v-list-item-title>

          </v-list-item>
      </v-list>

    </v-navigation-drawer>

    <!-- TOOLBAR -->
    <v-app-bar>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Wagtail / NuxtJS / Graphene / Vuetify</v-toolbar-title>
    </v-app-bar>

    <!-- MAIN FRAME -->
    <v-main>


      <!-- NOTICE -->
      <v-col class="text-center mx-auto" cols="6">
        <v-alert
          closable
          title="Notice"
          text="Please take a look at README.md and all config files. :)"
          type="warning"
          variant="outlined"
        ></v-alert>

        <!-- WELCOME TEXT -->


        <!-- NEWS CARD -->
        <v-card v-model="article" variant="outlined" class="mx-auto mt-10">
          <v-card-title class="text-secondary">{{ article.title }}</v-card-title>
          <v-card-subtitle>{{ article.date }}</v-card-subtitle>
          <v-card-text>
            <p>{{ article.intro }}</p>
            <p>{{ article.body }}</p>
          </v-card-text>
        </v-card>

        <v-btn @click="refresh(query)"
          color="secondary"
          elevation="5"
          x-large
          class="mx-auto d-block my-5"
        >re-fetch data from API</v-btn>

        <a href="http://localhost:7999/admin" class="text-decoration-none secondary" target="_blank">open Wagtail admin panel</a><br>
        <a href="http://localhost:7999/api/graphiql/" class="text-decoration-none secondary">open GraphgQL console</a>
        


      </v-col>
    </v-main>

    <v-footer padless>
      <v-col class="text-center mx-auto" cols="6">
        <p class="text-subtitle-2 text-primary font-weight-light">cooked together by ordigital in 2023</p>
      </v-col>
    </v-footer>

  </v-app>
</div>
</template>


<script lang="ts" setup>
  import articlesQuery from '~/apollo/queries/articles.graphql'
  // get example data (you must add some NewsPages in Wagtail admin panel to work)
  const query = articlesQuery; // or inline query: gql`query articles { articles { title intro }}`
  const { data, error, refresh } = await useAsyncQuery(query);
  // forced refresh because I dunno why it's not fetching anything
  // after opening or refreshing page in browser
  refresh(query);
</script>

<script lang="ts">
  export default {
    data: () => ({ 
      drawer: true,
      article: {
        title: "Choose article from menu",
        date: "Article date will show up here",
        body: "Article body will replace this text.",
      },
    }),

    methods: {
      getPost(event) {
        this.article = event;
      }
    }
  }


</script>
