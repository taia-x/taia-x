<template>
  <button
    @click.prevent="buyToken"
    v-if="token && token.price"
    class="inline-flex items-center justify-center px-3 text-white transition duration-300 ease-in-out transform border-2 border-b-4 rounded-md h-10 bg-cyan-500 hover:bg-cyan-600 text-md whitespace-nowrap border-cyan-700 hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500 disabled:cursor-not-allowed disabled:bg-gray-100 disabled:border-gray-300 disabled:text-gray-400"
    :disabled="
      token.cert_state === 'pending' ||
      token.cert_state === 'rejected' ||
      user.role !== 'consumer'
    "
  >
    Buy for {{ token.price / 1000000 }} ꜩ
  </button>
</template>

<script>
import { defineComponent } from "vue";
import { tezosInterface } from "@/services";
import { useAlertStore } from "@/stores/useAlerts";

export default defineComponent({
  props: {
    token: {
      type: Object,
      required: true,
    },
    user: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const alerts = useAlertStore();

    const buyToken = async () => {
      try {
        await tezosInterface.buy(props.token.price, props.token.id);
        // notifies user and resets values
        alerts.createAlert("Successfully purchased NFT!", "success");
      } catch (e) {
        alerts.createAlert("Something went wrong!", "error");
        throw new Error(e.toString());
      }
    };

    return {
      buyToken,
    };
  },
});
</script>
