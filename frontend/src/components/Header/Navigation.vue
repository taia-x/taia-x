<template>
  <div class="flex items-center justify-between w-full">
    <nav class="flex items-center">
      <router-link
        to="/"
        class="text-lg font-semibold leading-7 text-gray-700 transition duration-300 ease-in-out hover:text-cyan-500"
        >Taia-X<span class="font-mono text-xs text-gray-600 font-extralight"
          >&nbsp;A Blockchain Marketplace for Digital Twin Data</span
        ></router-link
      >
    </nav>
    <nav class="flex items-center space-x-6">
      <router-link
        to="/explore"
        class="flex items-center space-x-2 transition duration-200 ease-in-out hover:text-cyan-500"
        v-slot="{ isActive, isExactActive }"
      >
        <SearchIcon
          class="w-5 h-5"
          :class="isActive && isExactActive ? 'text-cyan-500' : ''"
        />
        <span :class="isActive && isExactActive ? 'text-cyan-500' : ''">
          Explore
        </span>
      </router-link>
      <router-link
        to="/create"
        class="flex items-center space-x-2 transition duration-200 ease-in-out h-9 hover:text-cyan-500"
        v-if="address && role === 'provider'"
      >
        <div
          v-if="address"
          class="flex items-center justify-center px-3 text-white transition duration-300 ease-in-out transform border-2 border-b-4 rounded-md h-10 bg-cyan-500 hover:bg-cyan-600 text-md whitespace-nowrap border-cyan-700 hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
        >
          <PlusIcon class="w-5 h-5 transform -translate-x-1" />
          Create
        </div>
      </router-link>
    </nav>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { SearchIcon, PlusIcon } from "@heroicons/vue/outline";

export default defineComponent({
  components: {
    SearchIcon,
    PlusIcon,
  },
  props: {
    address: {
      type: String,
      required: true,
    },
    role: {
      type: String,
      required: true,
    },
  },
});
</script>
