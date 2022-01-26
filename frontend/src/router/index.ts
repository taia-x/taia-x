import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import { useUserStore } from "@/stores/useUser";
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
    path: "/create",
    name: "Create",
    component: () =>
      import(/* webpackChunkName: "create" */ "@/views/Create.vue"),
  },
  {
    path: "/explore/:id",
    name: "ExplorerDetails",
    component: () =>
      import(
        /* webpackChunkName: "explorer-details" */ "@/views/ExplorerDetails.vue"
      ),
  },
  {
    path: "/profile/:address",
    name: "ProfileDetails",
    component: () =>
      import(/* webpackChunkName: "profile-details" */ "@/views/ProfileDetails.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// navigation guard to ensure provider role to be able to access /create route
// router.beforeEach((to, from, next) => {
//   const user = useUserStore();
//   if (to.name === "Create" && user.getRole !== "provider")
//     next({ name: "Explorer" });
//   else next();
// });

export default router;
