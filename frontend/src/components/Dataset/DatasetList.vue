<template>
  <div></div>
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
