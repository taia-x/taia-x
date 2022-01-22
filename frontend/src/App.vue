<template>
  <Header
    @update:isOpen="isRegisterModalOpen = $event"
    class="fixed top-0 z-10 bg-white"
  />
  <div class="h-24"></div>
  <div class="relative w-full max-w-6xl mx-auto">
    <router-view />
  </div>
  <AlertWrapper />
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import Header from "@/components/Header/Header.vue";
import AlertWrapper from "@/components/Utils/AlertWrapper.vue";
import { useUserStore } from "@/stores/useUser";
import initInterfaces from "@/services";

export default defineComponent({
  components: {
    Header,
    AlertWrapper,
  },
  setup() {
    const user = useUserStore();
    const { initializeUser } = user;

    onMounted(async () => {
      try {
        await initInterfaces();
        await initializeUser();
      } catch (e: any) {
        throw new Error(e.toString());
      }
    });
  },
});
</script>
