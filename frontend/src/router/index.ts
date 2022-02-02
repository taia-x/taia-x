import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Explorer from "@/views/Explorer.vue";
import { useUserStore } from "@/stores/useUser";

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
        redirect: { name: "created" },
      },
      {
        path: "created",
        name: "created",
        component: () =>
          import(
            /* webpackChunkName: "created" */ "@/views/ProfileDetailsTabs/Created.vue"
          ),
      },
      {
        path: "collected",
        name: "collected",
        component: () =>
          import(
            /* webpackChunkName: "created" */ "@/views/ProfileDetailsTabs/Collected.vue"
          ),
      },
      {
        path: "certified",
        name: "certified",
        component: () =>
          import(
            /* webpackChunkName: "created" */ "@/views/ProfileDetailsTabs/Certified.vue"
          ),
      },
      {
        path: "activity",
        name: "activity",
        component: () =>
          import(
            /* webpackChunkName: "created" */ "@/views/ProfileDetailsTabs/Activity.vue"
          ),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// navigation guard to ensure provider role to be able to access /create route
router.beforeEach((to, from, next) => {
  const user = useUserStore();
  if (to.name === "Create" && user.role !== "provider")
    next({ name: "Explorer" });
  if (to.name === "certified" && user.role !== "certifier") next(false);
  else next();
});

export default router;
