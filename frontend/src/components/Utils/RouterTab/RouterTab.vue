<template>
  <TabPanel :key="to" :class="['py-8 grid grid-cols-4 gap-6']">
    <slot></slot>
  </TabPanel>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { TabPanel } from "@headlessui/vue";

export default defineComponent({
  components: {
    TabPanel,
  },
  props: {
    title: String,
    to: String,
  },
});
</script>
