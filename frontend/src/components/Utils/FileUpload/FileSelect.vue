<template>
  <div
    class="flex justify-center px-6 pt-5 pb-6 mt-1 border-2 border-gray-300 border-dashed rounded-md "
    @drop.prevent="$emit('fileSelected')"
    @dragover.prevent
  >
    <div class="space-y-1 text-center">
      <CloudUploadIcon class="mx-auto text-gray-400 w-11 h-11 heroicon-sw-1" />
      <div class="flex text-sm text-gray-600">
        <label
          for="file-upload"
          class="relative font-medium bg-white rounded cursor-pointer  text-cyan-500 hover:text-cyan-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-cyan-500"
        >
          <span>Upload a file</span>
          <input
            id="file-upload"
            name="file-upload"
            type="file"
            accept=".json"
            class="sr-only"
            @change="$emit('fileSelected', $event)"
          />
        </label>
        <p class="pl-1">or drag and drop</p>
      </div>
      <p class="text-xs text-gray-500">.JSON up to 10MB</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { CloudUploadIcon } from "@heroicons/vue/outline";

export default defineComponent({
  components: {
    CloudUploadIcon,
  },
});
</script>

<style>
.heroicon-sw-1 path {
  stroke-width: 1.2 !important;
}
</style>
