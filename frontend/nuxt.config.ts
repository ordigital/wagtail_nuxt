const srvCfg = process.env.NODE_DEV !== 'production' ? 
    { 
        proxy: { 
            '/api':         'http://localhost:7999',
            '/admin':       'http://localhost:7999',
            '/django-admin':'http://localhost:7999',
            '/static':      'http://localhost:7999',
        } 
    } : {};

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
                httpEndpoint: '/api/graphql',
                websocketsOnly: false,
                connectToDevTools: true,
                tokenStorage: 'cookie',
                // authType: 'Bearer',
                // authHeader: 'Authorization',
                // tokenName: "wagtail-token",
            }
        },
    },

    vite: {
        define: {
          'process.env.DEBUG': false,
        },
         server: srvCfg,
    }



})
