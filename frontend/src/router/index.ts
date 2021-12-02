import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Explorer from "../views/Explorer.vue";
import Ontologies from "../views/Ontologies.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    redirect: "/explore",
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/explore",
  },
  {
    path: "/explore",
    name: "Explorer",
    component: Explorer,
  },
  {
    path: "/ontologies",
    name: "Ontologies",
    component: Ontologies,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
