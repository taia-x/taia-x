<template>
  <div
    class="flex items-center justify-between w-full p-2 mt-1 rounded-md  bg-gray-50"
  >
    <div class="flex items-center space-x-2">
      <DocumentTextIcon class="w-5 h-5 text-gray-700" />
      <span class="font-mono text-sm truncate">{{ fileName }}</span>
    </div>
    <XIcon
      class="w-5 h-5 text-right text-gray-400 cursor-pointer  hover:text-gray-700"
      @click.prevent="$emit('fileRemoved')"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { DocumentTextIcon } from "@heroicons/vue/outline";
import { XIcon } from "@heroicons/vue/solid";

export default defineComponent({
  components: {
    DocumentTextIcon,
    XIcon,
  },
  props: {
    fileName: {
      type: String,
      required: true,
    },
  },
});
</script>
