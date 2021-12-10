import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import VWave from "v-wave";
import { createPinia } from "pinia";
import "./assets/css/tailwind.css";
import "./assets/css/fonts.css";
import { useUserStore } from "@/stores/useUser";
import initInterfaces from "@/services";

const app = createApp(App);
app.use(createPinia()).use(router).use(VWave);

const user = useUserStore();
const { initializeUser } = user;

/**
 * start app by initializing user first
 */
const startApp = async () => {
  try {
    await initInterfaces();
    await initializeUser();
  } catch (e) {
    throw new Error("Unable to initialize App!");
  }
  app.mount("#app");
};

startApp();
