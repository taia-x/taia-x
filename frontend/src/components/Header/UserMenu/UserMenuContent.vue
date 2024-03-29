<template>
  <div class="flex flex-col items-center p-1.5 w-48">
    <div class="grid grid-cols-1 space-y-1.5 text-gray-600 w-full">
      <div class="border-b-2">
        <router-link
          :to="profileUrl + '/collected'"
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100 space-x-2 hover:text-gray-800 transition-colors duration-100 ease-out"
        >
          <CollectionIcon class="absolute w-5 h-5 left-2" />
          Collected
        </router-link>
      </div>
      <div class="border-b-2">
        <router-link
          :to="profileUrl + '/created'"
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100 hover:text-gray-800 transition-colors duration-100 ease-out"
        >
          <DocumentAddIcon class="absolute w-5 h-5 left-2" />
          Created
        </router-link>
      </div>
      <div class="border-b-2">
        <router-link
          :to="profileUrl + '/certified'"
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100 hover:text-gray-800 transition-colors duration-100 ease-out"
        >
          <BadgeCheckIcon class="absolute w-5 h-5 left-2" />
          Certified
        </router-link>
      </div>
      <div class="border-b-2">
        <router-link
          :to="profileUrl + '/activity'"
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100 hover:text-gray-800 transition-colors duration-100 ease-out"
        >
          <ClockIcon class="absolute w-5 h-5 left-2" />
          Activity
        </router-link>
      </div>
      <div class="border-b-2">
        <router-link
          :to="profileUrl + '/downloads'"
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100 hover:text-gray-800 transition-colors duration-100 ease-out"
        >
          <DownloadIcon class="absolute w-5 h-5 left-2" />
          Downloads
        </router-link>
      </div>
      <div>
        <button
          @click.prevent="disconnect()"
          class="relative flex justify-center w-full px-12 py-2 font-medium text-center transition-colors duration-100 ease-out rounded-md cursor-pointer hover:bg-gray-100 hover:text-gray-800"
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
  DownloadIcon,
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
    DownloadIcon,
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

    const profileUrl = `/profile/${props.address}`;

    return { disconnect, copyToClipboard, isOpen, profileUrl };
  },
});
</script>
