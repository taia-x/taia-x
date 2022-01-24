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
import { defineComponent, onMounted } from "vue";
import Header from "@/components/Header/Header.vue";
import AlertWrapper from "@/components/Utils/AlertWrapper.vue";
import { useUserStore } from "@/stores/useUser";
import initInterfaces from "@/services";
import { storeToRefs } from "pinia";
import { HTTP_METADATA_API_URL } from "@/constants";

export default defineComponent({
  components: {
    Header,
    AlertWrapper,
  },
  setup() {
    const user = useUserStore();
    const { initializeUser } = user;
    const { address } = storeToRefs(user);

    const setRole = async () => {
      const result = await fetch(HTTP_METADATA_API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: `
              query GetAccount($address: String = "") {
                account_by_pk(address: $address) {
                  address
                  role
                }
              }
            `,
          variables: {
            address: address.value,
          },
        }),
      });
      const { data } = await result.json();
      user.$patch((state) => (state.role = data.account_by_pk.role));
    };

    onMounted(async () => {
      try {
        await initInterfaces();
        await initializeUser();
        if (address.value) setRole();
      } catch (e: any) {
        throw new Error(e.toString());
      }
    });
  },
});
</script>
