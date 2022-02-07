<template>
  <div class="flex flex-col justify-between h-56 p-4">
    <div>
      <div class="flex items-center justify-between">
        <span class="flex items-center space-x-2"
          ><span
            class="w-8 h-8 rounded-full left-2.5 bg-gray-100 animate-pulse"
            :style="
              index > 8
                ? 'animation-delay: 300ms; animation-fill-mode: backwards'
                : index > 4
                ? 'animation-delay: 150ms; animation-fill-mode: backwards'
                : ''
            " />
          <span
            class="w-20 h-5 bg-gray-100 rounded-md animate-pulse"
            :style="
              index > 8
                ? 'animation-delay: 300ms; animation-fill-mode: backwards'
                : index > 4
                ? 'animation-delay: 150ms; animation-fill-mode: backwards'
                : ''
            "
        /></span>
      </div>
      <div class="flex items-center mt-4">
        <span
          class="w-32 h-5 bg-gray-100 rounded-md animate-pulse"
          :style="
            index > 8
              ? 'animation-delay: 300ms; animation-fill-mode: backwards'
              : index > 4
              ? 'animation-delay: 150ms; animation-fill-mode: backwards'
              : ''
          "
        />
      </div>
      <div class="flex flex-col items-start mt-4 space-y-1">
        <span
          class="w-full h-5 bg-gray-100 rounded-md animate-pulse"
          :style="
            index > 8
              ? 'animation-delay: 300ms; animation-fill-mode: backwards'
              : index > 4
              ? 'animation-delay: 150ms; animation-fill-mode: backwards'
              : ''
          "
        />
        <span
          class="w-48 h-5 bg-gray-100 rounded-md animate-pulse"
          :style="
            index > 8
              ? 'animation-delay: 300ms; animation-fill-mode: backwards'
              : index > 4
              ? 'animation-delay: 150ms; animation-fill-mode: backwards'
              : ''
          "
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    index: {
      type: Number,
      required: true,
    },
  },
});
</script>
