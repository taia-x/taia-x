<template>
  <div
    class="z-50 flex items-center justify-between w-full h-24 px-10 py-4 mx-auto font-sans text-sm font-medium text-gray-900 border-gray-200 bg-opacity-5 backdrop-filter backdrop-blur"
  >
    <div class="flex items-center w-full space-x-6">
      <Navigation :address="address" :role="role" />
      <div class="flex items-center h-9">
        <SignInButton :address="address" />
        <HatMenu :address="address" />
      </div>
      <UserMenu :address="address" :privateAddress="getPrivatizedAddress" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import Navigation from "@/components/Header/Navigation.vue";
import SignInButton from "@/components/Header/SignInButton.vue";
import UserMenu from "@/components/Header/UserMenu/UserMenu.vue";
import HatMenu from "@/components/Header/HatMenu/HatMenu.vue";
import { useUserStore } from "@/stores/useUser";
import { storeToRefs } from "pinia";

export default defineComponent({
  components: {
    Navigation,
    SignInButton,
    UserMenu,
    HatMenu,
  },
  setup() {
    const user = useUserStore();
    const { address, role } = storeToRefs(user);

    // does not reveal full address in ui
    const getPrivatizedAddress = computed(() => {
      return `${address.value.substring(0, 5)}...${address.value.substring(
        address.value.length - 5,
        address.value.length
      )}`;
    });

    return { address, role, getPrivatizedAddress };
  },
});
</script>
