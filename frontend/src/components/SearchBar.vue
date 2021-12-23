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
      class="block w-full pl-12 transition duration-300 border-2 border-gray-300 rounded-md  h-11 focus:ring-cyan-500 focus:border-cyan-500"
    />
  </div>
  <button
    v-wave
    class="
      flex
      items-center
      justify-center
      px-3
      py-2
      text-white
      transition
      duration-300
      ease-in-out
      transform
      border-2 border-b-4
      rounded-md
      h-11
      bg-cyan-500
      hover:bg-cyan-600
      text-md
      whitespace-nowrap
      border-cyan-700
      hover:-translate-y-0.5
      focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500
    "
    @click.prevent="$emit('create:clicked')"
  >
    <PlusIcon class="w-5 h-5 transform -translate-x-1" />
    <span>Create</span>
  </button>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { SearchIcon, PlusIcon } from "@heroicons/vue/solid";

export default defineComponent({
  components: {
    SearchIcon,
    PlusIcon,
  },
});
</script>
