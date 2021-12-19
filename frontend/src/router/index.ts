import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Explorer from "@/views/Explorer.vue";

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
    component: () =>
      import(/* webpackChunkName: "ontologies" */ "@/views/Ontologies.vue"), // lazy loading
  },
  {
    path: "/explore/:id",
    name: "ExplorerDetails",
    component: () =>
      import(
        /* webpackChunkName: "explorer-details" */ "@/views/ExplorerDetails.vue"
      ), // lazy loading
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
