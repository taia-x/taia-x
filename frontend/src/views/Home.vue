<template>
  <div></div>
  <!-- <div>
    <div class="flex justify-center p-4 space-x-2 home">
      <button
        v-wave
        class="flex items-center justify-center px-4 py-3 font-semibold text-blue-100 bg-blue-700 rounded-lg text-md focus:outline-none focus-visible:ring-2 hover:bg-blue-800 focus-visible:ring-blue-600"
        @click.prevent="connectToWallet()"
      >
        <CloudIcon class="w-5 h-5 text-blue-100" />

        <span class="pl-1 text-blue-100 text-md">Connect Wallet</span>
      </button>
      <button
        v-wave
        class="flex items-center justify-center px-4 py-3 font-semibold text-red-100 bg-red-700 rounded-lg text-md focus:outline-none focus-visible:ring-2 hover:bg-red-800 focus-visible:ring-red-600"
        @click.prevent="disconnectFromWallet()"
      >
        <span class="pl-1 text-red-100 text-md">Disconnect Wallet</span>
      </button>
      <button
        v-wave
        class="flex items-center justify-center px-4 py-3 font-semibold text-teal-100 bg-teal-700 rounded-lg text-md focus:outline-none focus-visible:ring-2 hover:bg-teal-800 focus-visible:ring-teal-600"
        @click.prevent="sendIncrement()"
      >
        <span class="pl-1 text-teal-100 text-md">Increment</span>
      </button>
    </div>
    <div class="flex items-center justify-center text-2xl text-white">
      Amount: {{ amount }}
    </div>
  </div> -->
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
// import {
//   connectWallet,
//   disconnectWallet,
//   increment,
//   getContractStorage,
// } from "@/services/wallet-service";
// import { CloudIcon } from "@heroicons/vue/solid";
// import { useUserStore } from "@/stores/useUser";
// import { storeToRefs } from "pinia";

export default defineComponent({
  //   name: "Home",
  //   components: { CloudIcon },
  //   setup() {
  //     const main = useUserStore();
  //     const { address, balance } = storeToRefs(main);
  //     const amount = ref(0);
  //     onMounted(async () => {
  //       const storage = await getContractStorage();
  //       amount.value = storage.toNumber();
  //     });
  //     const connectToWallet = async () => {
  //       await connectWallet();
  //     };
  //     const disconnectFromWallet = async () => {
  //       await disconnectWallet();
  //     };
  //     const sendIncrement = async () => {
  //       await increment();
  //       const storage = await getContractStorage();
  //       amount.value = storage.toNumber();
  //     };
  //     return {
  //       amount,
  //       main,
  //       address,
  //       balance,
  //       connectToWallet,
  //       disconnectFromWallet,
  //       sendIncrement,
  //     };
  //   },
});
</script>
