<template>
  <Header @update:isOpen="isOpen = $event" />
  <router-view />
  <RegisterModal :isOpen="isOpen" @update:isOpen="isOpen = $event" />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Header from "@/components/Header.vue";
import RegisterModal from "@/components/RegisterModal.vue";

export default defineComponent({
  components: {
    RegisterModal,
    Header,
  },
  setup() {
    const isOpen = ref(false);

    return { isOpen };
  },
});
</script>

<style>
body {
  @apply font-sans;
}
</style>
