<template>
  <div>
    <label for="description" class="block text-sm font-medium text-gray-700">
      Description
    </label>
    <div class="mt-1">
      <textarea
        v-model="description"
        tabindex="2"
        id="description"
        name="description"
        rows="6"
        class="block w-full mt-1 border border-gray-300 rounded-md shadow-sm focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
        placeholder="Provide a description of your dataset..."
        @change="$emit('update:description', description)"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const description = ref("");

    return {
      description,
    };
  },
});
</script>
