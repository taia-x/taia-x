import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Explorer from "@/views/Explorer.vue";
import Created from "@/views/ProfileDetailsTabs/Created.vue";
import Collected from "@/views/ProfileDetailsTabs/Collected.vue";
import Certified from "@/views/ProfileDetailsTabs/Certified.vue";
import Activity from "@/views/ProfileDetailsTabs/Activity.vue";

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
      import(
        /* webpackChunkName: "profile-details" */ "@/views/ProfileDetails.vue"
      ),
    props: true,
    children: [
      {
        path: "",
        component: Created,
      },
      {
        path: "created",
        component: Created,
      },
      {
        path: "collected",
        component: Collected,
      },
      {
        path: "certified",
        component: Certified,
      },
      {
        path: "activity",
        component: Activity,
      },
    ],
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
