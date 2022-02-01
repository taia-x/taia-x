<template>
  <div class="container mx-auto space-y-8">
    <div class="flex items-center space-x-8">
      <div>
        <img
          :src="`${ACCOUNT_IMAGE_PATH}${address}`"
          class="h-32 w-32 rounded-full"
        />
      </div>
      <h1>{{ address }}</h1>
    </div>
    <div>
      <ul class="flex border-b space-x-10">
        <router-link
          v-for="title in tabs"
          :key="title"
          :to="title.toLowerCase()"
          v-slot="{ href, navigate, isExactActive }"
        >
          <li class="block relative">
            <a
              :class="[
                'block py-4 text-black font-semibold transition duration-300 ease-in-out capitalize text-opacity-25 hover:text-opacity-100',
                isExactActive && 'text-opacity-100',
              ]"
              :href="href"
              @click="navigate"
            >
              {{ title }}</a
            >
            <span
              aria-hidden="true"
              :class="[
                'block absolute w-full h-0.5 -bottom-0.5 left-0 transition duration-300 ease-in-out',
                isExactActive ? 'bg-cyan-500' : 'bg-transparent',
              ]"
            ></span>
          </li>
        </router-link>
      </ul>

      <div class="mt-2 py-8">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import { ACCOUNT_IMAGE_PATH } from "@/constants";

export default defineComponent({
  setup() {
    const route = useRoute();
    const address = route.params.address;

    const tabs = ["collected", "created", "certified", "activity"];

    return {
      route,
      tabs,
      ACCOUNT_IMAGE_PATH,
      address,
    };
  },
});
</script>
