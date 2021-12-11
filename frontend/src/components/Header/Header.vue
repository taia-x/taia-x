<template>
  <div
    class="flex items-center justify-between w-full px-10 py-8 mx-auto font-sans text-sm font-medium text-gray-900 border-gray-200 "
  >
    <nav>
      <router-link
        to="/"
        class="text-lg font-semibold leading-7 text-gray-700 transition duration-300 ease-in-out  hover:text-cyan-500"
        >Taia-X<span class="font-mono text-xs text-gray-600 font-extralight"
          >&nbsp;A Blockchain Marketplace for Digital Twin Data</span
        ></router-link
      >
    </nav>
    <div class="flex items-center space-x-6">
      <Navigation />
      <div class="flex items-center space-x-2">
        <SignInButton :address="address" />
        <SignUpButton
          :address="address"
          @update:isOpen="$emit('update:isOpen', true)"
        />
        <AccountToggle
          :address="address"
          :privateAddress="getPrivatizedAddress"
          :balance="balance"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import Navigation from "@/components/Header/Navigation.vue";
import SignInButton from "@/components/Header/SignInButton.vue";
import SignUpButton from "@/components/Header/SignUpButton.vue";
import AccountToggle from "@/components/Header/Account/AccountToggle.vue";
import { useUserStore } from "@/stores/useUser";
import { storeToRefs } from "pinia";

export default defineComponent({
  components: {
    Navigation,
    SignInButton,
    SignUpButton,
    AccountToggle,
  },
  setup() {
    const user = useUserStore();
    const { address, balance } = storeToRefs(user);

    const getPrivatizedAddress = computed(() => {
      return `${address.value.substring(0, 5)}...${address.value.substring(
        address.value.length - 5,
        address.value.length
      )}`;
    });

    return { address, balance, getPrivatizedAddress };
  },
});
</script>
