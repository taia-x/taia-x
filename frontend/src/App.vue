<template>
  <Header
    @update:isOpen="isRegisterModalOpen = $event"
    class="fixed top-0 z-10 bg-white"
  />
  <div class="h-24"></div>
  <div class="relative w-full max-w-6xl mx-auto">
    <router-view />
  </div>
  <RegisterModal
    :isOpen="isRegisterModalOpen"
    @update:isOpen="isRegisterModalOpen = $event"
  />
  <AlertWrapper />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Header from "@/components/Header/Header.vue";
import RegisterModal from "@/components/RegisterModal.vue";
import AlertWrapper from "@/components/Utils/AlertWrapper.vue";

export default defineComponent({
  components: {
    RegisterModal,
    Header,
    AlertWrapper,
  },
  setup() {
    const isRegisterModalOpen = ref(false);

    return { isRegisterModalOpen };
  },
});
</script>
