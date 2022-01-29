<template>
  <router-link
    class="w-full transition duration-200 transform border-gray-300 rounded-lg bg-gray-50 hover:scale-105 h-96 focus:outline-none focus:ring-2 focus:ring-cyan-500"
    :to="'/explore/' + dataset.id"
  >
    <div class="flex flex-col p-4">
      <div class="grid grid-cols-2 gap-2">
        <span class="text-sm font-medium">owner</span>
        <span class="text-sm truncate">{{ dataset.creator_id }}</span>
        <span class="text-sm font-medium">id</span>
        <span class="text-sm truncate">{{ dataset.id }}</span>
        <span class="text-sm font-medium">metadata</span>
        <span class="text-sm truncate">{{ dataset.metadata }}</span>
      </div>
    </div>
  </router-link>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  components: {},
  props: {
    dataset: {
      type: Object,
      required: true,
    },
    index: {
      type: Number,
      required: true,
    },
  },
});
</script>
