<template>
  <div
    class="max-w-screen-lg mx-auto font-sans text-gray-800 xl:max-w-screen-xl"
  >
    <div
      class="flex items-center justify-between py-4 border-b border-gray-200"
    >
      <router-link to="/" class="text-lg font-thin leading-7 font-poppins"
        >Taia-X<span class="font-mono text-xs font-thin"
          >&nbsp;A Blockchain Marketplace for Digital Twin Data</span
        ></router-link
      >
      <div class="flex items-center space-x-4">
        <router-link
          to="/explore"
          class="px-3 py-2 rounded-md hover:bg-gray-100"
          >Explore</router-link
        >
        <router-link
          to="/certificates"
          class="px-3 py-2 rounded-md hover:bg-gray-100"
          >Certificates</router-link
        >
        <router-link
          to="/ontologies"
          class="px-3 py-2 rounded-md hover:bg-gray-100"
          >Ontologies</router-link
        >
      </div>
    </div>
  </div>

  <router-view />
</template>

<script>
import { font as poppinsBold } from "../public/fonts/generated/Poppins-Bold.module.css";
import { defineComponent } from "vue";

export default defineComponent({
  setup() {
    return { poppinsBold };
  },
});
</script>

<style>
body {
  @apply dark:bg-background font-sans;
}
</style>
