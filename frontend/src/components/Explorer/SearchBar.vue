<template>
  <div class="relative w-full group">
    <span class="absolute inset-y-0 left-0 flex items-center pl-4 group">
      <SearchIcon class="w-5 h-5 text-gray-500" />
    </span>
    <input
      type="text"
      name="first-name"
      id="first-name"
      autocomplete="given-name"
      placeholder="Search"
      class="block w-full pl-12 transition duration-300 border-2 border-gray-300 rounded-md h-11 focus:ring-cyan-500 focus:border-cyan-500"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { SearchIcon } from "@heroicons/vue/solid";

export default defineComponent({
  components: {
    SearchIcon,
  },
});
</script>
