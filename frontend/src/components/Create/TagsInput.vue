<template>
  <div>
    <label for="name" class="block text-sm font-medium text-gray-700">
      Tags
    </label>
    <div class="flex w-full mt-1 rounded-md shadow-sm">
      <input
        v-model="tags"
        tabindex="3"
        autofocus
        type="text"
        name="name"
        id="name"
        class="flex-1 block w-full border-gray-300 rounded-md focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
        placeholder="Comma separated list"
        @change="$emit('update:tags', tags)"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const tags = ref("");

    return {
      tags,
    };
  },
});
</script>
