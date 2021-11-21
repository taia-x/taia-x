<template>
  <div
    class="max-w-screen-lg mx-auto font-sans text-gray-800 xl:max-w-screen-xl"
  >
    <div
      class="flex items-center justify-between py-4 border-b border-gray-200"
    >
      <router-link to="/" class="text-lg font-semibold leading-7"
        >Taia-X<span class="font-mono text-xs font-thin"
          >&nbsp;A Blockchain Marketplace for Digital Twin Data</span
        ></router-link
      >
      <div class="flex items-center space-x-4">
        <router-link
          v-wave
          to="/explore"
          class="px-3 py-2 rounded-md hover:bg-gray-100"
          >Explore</router-link
        >
        <router-link
          v-wave
          to="/certificates"
          class="px-3 py-2 rounded-md hover:bg-gray-100"
          >Certificates</router-link
        >
        <router-link
          v-wave
          to="/ontologies"
          class="px-3 py-2 rounded-md hover:bg-gray-100"
          >Ontologies</router-link
        >
        <div class="flex items-center space-x-2">
          <button
            v-wave
            class="flex items-center justify-center px-3 py-2 font-semibold text-gray-400 transition duration-300 ease-in-out bg-gray-100 rounded-md  text-md focus:outline-none focus-visible:ring-2 hover:bg-gray-200 focus-visible:ring-blue-400 hover:text-gray-700"
            @click.prevent="connectToWallet()"
          >
            <span class="pl-1">Connect Wallet</span>
          </button>
          <button
            v-wave
            class="flex items-center justify-center px-3 py-2 font-semibold text-gray-400 transition duration-300 ease-in-out bg-gray-100 rounded-md  text-md focus:outline-none focus-visible:ring-2 hover:bg-gray-200 focus-visible:ring-blue-400 hover:text-gray-700"
            @click.prevent="isOpen = true"
          >
            <span class="pl-1">Register</span>
          </button>
        </div>
      </div>
    </div>
  </div>
  <RegisterModal :isOpen="isOpen" @update:isOpen="isOpen = $event" />
  <router-view />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import RegisterModal from "@/components/RegisterModal.vue";

export default defineComponent({
  components: {
    RegisterModal,
  },
  setup() {
    const isOpen = ref(false);

    return { isOpen };
  },
});
</script>

<style>
body {
  @apply font-sans;
}
</style>
