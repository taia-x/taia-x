import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VWave from "v-wave";
import { createPinia } from "pinia";
import "./assets/css/tailwind.css";

createApp(App).use(createPinia()).use(router).use(VWave).mount("#app");
