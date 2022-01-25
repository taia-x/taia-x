import { createApp, provide, h } from "vue";
import { ApolloClients } from "@vue/apollo-composable";
import { tokenMetadataClient } from "@/services/TokenMetadata";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";
import "./assets/css/tailwind.css";
import "./assets/css/fonts.css";

const app = createApp({
  setup() {
    provide(ApolloClients, {
      default: tokenMetadataClient,
    });
  },
  render: () => h(App),
});
app.use(createPinia()).use(router).mount("#app");
