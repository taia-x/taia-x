import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VWave from "v-wave";
import { createPinia } from "pinia";
import "./assets/css/tailwind.css";
import "./assets/css/fonts.css";
import { useUserStore } from "@/stores/useUser";

const app = createApp(App);
app.use(createPinia()).use(router).use(VWave);

const user = useUserStore();
const { initializeUser } = user;

const startApp = async () => {
  try {
    await initializeUser();
  } catch (e) {
    console.log(e);
  }
  app.mount("#app");
};

startApp();
