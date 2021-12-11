<template>
  <button
    v-if="!address"
    v-wave
    class="flex items-center justify-center px-3 py-2 font-semibold text-white transition duration-300 ease-in-out bg-gray-900 rounded-md  text-md hover:bg-gray-700"
    @click.prevent="$emit('update:isOpen', true)"
  >
    <span>Sign up</span>
  </button>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    address: {
      type: String,
      requried: true,
    },
  },
});
</script>
