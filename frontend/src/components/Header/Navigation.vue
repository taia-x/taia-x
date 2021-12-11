<template>
  <nav class="flex items-center space-x-6">
    <router-link
      to="/explore"
      class="flex items-center space-x-2 transition duration-300 ease-in-out  hover:text-cyan-500"
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
      to="/ontologies"
      class="flex items-center space-x-2 transition duration-300 ease-in-out  hover:text-cyan-500"
      v-slot="{ isActive, isExactActive }"
    >
      <BookOpenIcon
        class="w-5 h-5"
        :class="isActive && isExactActive ? 'text-cyan-500' : ''"
      />
      <span :class="isActive && isExactActive ? 'text-cyan-500' : ''">
        Ontologies
      </span>
    </router-link>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { SearchIcon, BookOpenIcon } from "@heroicons/vue/outline";

export default defineComponent({
  components: {
    SearchIcon,
    BookOpenIcon,
  },
});
</script>
