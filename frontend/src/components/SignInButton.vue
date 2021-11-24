<template>
  <button
    v-if="!address"
    v-wave
    class="flex items-center justify-center px-3 py-2 font-semibold text-gray-500 transition duration-300 ease-in-out bg-gray-100 rounded-md  hover:text-gray-900 text-md"
    @click.prevent="connect()"
  >
    <span class="pl-1">Sign in</span>
  </button>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { tezosInterface } from "@/services/index";
import { useUserStore } from "@/stores/useUser";

export default defineComponent({
  props: {
    address: {
      type: String,
      required: true,
    },
  },
  setup() {
    const user = useUserStore();
    const { initializeUser } = user;

    const connect = async (): Promise<void> => {
      await tezosInterface.connectWallet();
      await initializeUser();
    };

    return { connect };
  },
});
</script>
