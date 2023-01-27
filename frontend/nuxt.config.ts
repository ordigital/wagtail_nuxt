export default({
        


    modules: ['@nuxtjs/apollo'],
    
    css: [
        'vuetify/styles',
        'vuetify/lib/styles/main.sass',
        '@mdi/font/css/materialdesignicons.css',
    ],

    build: {
      transpile: ['vuetify'],
    },
       
    buildModules: [
        //
    ],

    apollo: {
        clients: {
            default: {
                httpEndpoint: process.env.MAIN_URL + '/api/graphql' || 'http://localhost:7999/api/graphql', // remember to change later
                websocketsOnly: false,
                connectToDevTools: true,
                tokenStorage: 'cookie',
                authType: 'Bearer',
                authHeader: 'Authorization',
                tokenName: "wagtail-token",
            }
        },
    },

    vite: {
        define: {
          'process.env.DEBUG': false,
        },
    },




})
