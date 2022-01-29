<template>
  <div class="space-y-4">
    <h3 class="flex items-center space-x-1 text-xl font-semibold text-gray-900">
      <slot name="title"></slot>
      <InformationCircleIcon
        class="w-5 h-5 text-gray-400 transform -translate-y-1"
      />
    </h3>
    <slot name="content"></slot>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { InformationCircleIcon } from "@heroicons/vue/outline";

export default defineComponent({
  components: {
    InformationCircleIcon,
  },
});
</script>
