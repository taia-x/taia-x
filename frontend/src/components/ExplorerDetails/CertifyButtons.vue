<template>
  <div class="flex items-center space-x-2">
    <button
      @click.prevent="certifyDataset('certify')"
      class="inline-flex items-center justify-center px-3 text-white transition duration-300 ease-in-out transform border-2 border-b-4 rounded-md h-10 bg-cyan-500 hover:bg-cyan-600 text-md whitespace-nowrap border-cyan-700 hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500 disabled:cursor-not-allowed disabled:bg-gray-100 disabled:border-gray-300 disabled:text-gray-400"
      :disabled="
        token.cert_state === 'rejected' ||
        token.cert_state === 'certified' ||
        user.role !== 'certifier'
      "
    >
      <BadgeCheckIcon class="w-5 h-5" />
      <span>Certify</span>
    </button>
    <button
      @click.prevent="certifyDataset('reject')"
      class="flex items-center space-x-2 justify-center px-3 text-white transition duration-300 ease-in-out transform border-2 border-b-4 rounded-md h-10 bg-red-500 hover:bg-red-600 text-md whitespace-nowrap border-red-700 hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 disabled:cursor-not-allowed disabled:bg-gray-100 disabled:border-gray-300 disabled:text-gray-400"
      :disabled="
        token.cert_state === 'rejected' ||
        token.cert_state === 'certified' ||
        user.role !== 'certifier'
      "
    >
      <BanIcon class="w-5 h-5" />
      <span>Reject</span>
    </button>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { tezosInterface } from "@/services";
import { useAlertStore } from "@/stores/useAlerts";
import { BadgeCheckIcon, BanIcon } from "@heroicons/vue/outline";

export default defineComponent({
  components: {
    BadgeCheckIcon,
    BanIcon,
  },
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
  setup(props, { emit }) {
    const alerts = useAlertStore();

    const certifyDataset = async (state) => {
      try {
        await tezosInterface.certify(state, props.token.id, props.token.hash);
        emit("update:cert_state", state);
        // notifies user and resets values
        alerts.createAlert(
          "Successfully updated certificate state!",
          "success"
        );
      } catch (e) {
        alerts.createAlert("Something went wrong!", "error");
        throw new Error(e.toString());
      }
    };

    return {
      certifyDataset,
    };
  },
});
</script>
