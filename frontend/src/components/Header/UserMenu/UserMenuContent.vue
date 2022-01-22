<template>
  <div class="flex flex-col items-center p-1.5 w-48">
    <div class="grid grid-cols-1 space-y-1.5 text-gray-700 w-full">
      <div class="border-b-2">
        <button
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100 space-x-2"
        >
          <CollectionIcon class="absolute w-5 h-5 left-2" />
          Collected
        </button>
      </div>
      <div class="border-b-2">
        <button
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100"
        >
          <DocumentAddIcon class="absolute w-5 h-5 left-2" />
          Created
        </button>
      </div>
      <div class="border-b-2">
        <button
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100"
        >
          <BadgeCheckIcon class="absolute w-5 h-5 left-2" />
          Certified
        </button>
      </div>
      <div class="border-b-2">
        <button
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100"
        >
          <ClockIcon class="absolute w-5 h-5 left-2" />
          Activity
        </button>
      </div>
      <div>
        <button
          @click.prevent="disconnect()"
          class="relative flex justify-center w-full px-12 py-2 font-medium text-center rounded-md cursor-pointer hover:bg-gray-100"
        >
          <LogoutIcon class="absolute w-5 h-5 left-2.5" />
          Logout
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { walletInterface } from "@/services/index";
import { useUserStore } from "@/stores/useUser";
import {
  CollectionIcon,
  BadgeCheckIcon,
  DocumentAddIcon,
  LogoutIcon,
  ClockIcon,
} from "@heroicons/vue/outline";

export default defineComponent({
  props: {
    address: {
      type: String,
      requried: true,
    },
    privateAddress: {
      type: String,
      requried: true,
    },
  },
  components: {
    CollectionIcon,
    BadgeCheckIcon,
    DocumentAddIcon,
    LogoutIcon,
    ClockIcon,
  },
  setup(props) {
    const user = useUserStore();
    const isOpen = ref(false);

    const disconnect = async (): Promise<void> => {
      await walletInterface.disconnectWallet();
      await user.$reset();
    };

    const copyToClipboard = async (): Promise<void> => {
      try {
        isOpen.value = true;
        navigator.clipboard.writeText(props.address as string);
      } catch (e) {
        console.log(e);
      }
    };

    return { disconnect, copyToClipboard, isOpen };
  },
});
</script>
