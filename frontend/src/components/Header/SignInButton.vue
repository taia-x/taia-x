<template>
  <button
    v-if="!address"
    class="flex items-center justify-center px-3 text-white transition duration-300 ease-in-out transform border-2 border-b-4 rounded-md h-10 bg-cyan-500 hover:bg-cyan-600 text-md whitespace-nowrap border-cyan-700 hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500 font-medium"
    @click.prevent="connect()"
  >
    Sign in
  </button>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { walletInterface } from "@/services/index";
import { useUserStore } from "@/stores/useUser";
import { storeToRefs } from "pinia";
import { HTTP_METADATA_API_URL } from "@/constants";

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
      if (data?.account_by_pk?.role)
        user.$patch((state) => (state.role = data.account_by_pk.role));
    };

    const connect = async (): Promise<void> => {
      await walletInterface.connectWallet();
      await initializeUser();
      if (address.value) setRole();
    };

    return { connect };
  },
});
</script>
