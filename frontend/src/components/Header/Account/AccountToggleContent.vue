<template>
  <div class="flex flex-col items-center w-full">
    <div class="relative">
      <UserCircleIcon class="w-16 h-16 text-gray-300 rounded-full" />
      <span
        class="absolute bottom-0 right-0 w-2 h-2 transform -translate-x-2 -translate-y-2 bg-green-300 rounded-full  ring-2 ring-white"
      ></span>
    </div>
    <span class="w-full mt-2 text-2xl font-medium text-center text-gray-800"
      >{{ (balance / 1000000).toFixed(3)
      }}<span class="ml-1 text-lg font-medium">ꜩ</span></span
    >
    <button
      class="mt-2 font-semibold text-center text-gray-500 transition duration-150 select-none  hover:text-gray-700"
      @click.prevent="copyToClipboard()"
    >
      {{ privateAddress }}
    </button>
    <div class="grid w-full gap-2 pt-4 mt-4 border-t">
      <button
        class="flex items-center p-2 transition duration-150 ease-in-out rounded-lg  hover:bg-gray-100 group"
      >
        <div
          class="flex items-center justify-center flex-shrink-0 w-10 h-10 text-white transition duration-150 ease-in-out rounded-lg  bg-cyan-50 group-hover:bg-cyan-100 sm:h-12 sm:w-12"
        >
          <UserIcon class="w-5 h-5 text-cyan-700" />
        </div>
        <div class="ml-4">
          <p class="text-sm font-medium text-left text-gray-900">Profile</p>
          <p class="text-sm text-gray-500">View your profile</p>
        </div></button
      ><button
        class="flex items-center p-2 transition duration-150 ease-in-out rounded-lg  hover:bg-gray-100 group"
        @click.prevent="disconnect()"
      >
        <div
          class="flex items-center justify-center flex-shrink-0 w-10 h-10 text-white transition duration-150 ease-in-out rounded-lg  bg-cyan-50 group-hover:bg-cyan-100 sm:h-12 sm:w-12"
        >
          <LogoutIcon class="w-5 h-5 text-cyan-700" />
        </div>
        <div class="ml-4">
          <p class="text-sm font-medium text-left text-gray-900">Logout</p>
          <p class="text-sm text-gray-500">Disconnect from your wallet</p>
        </div>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { walletInterface } from "@/services/index";
import { useUserStore } from "@/stores/useUser";
import { UserCircleIcon, LogoutIcon, UserIcon } from "@heroicons/vue/solid";

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
    balance: {
      type: Number,
      required: true,
    },
  },
  components: {
    UserCircleIcon,
    LogoutIcon,
    UserIcon,
  },
  setup(props) {
    const user = useUserStore();

    const disconnect = async (): Promise<void> => {
      await walletInterface.disconnectWallet();
      await user.$reset();
    };

    const copyToClipboard = async (): Promise<void> => {
      try {
        navigator.clipboard.writeText(props.address as string);
      } catch (e) {
        console.log(e);
      }
    };

    return { disconnect, copyToClipboard };
  },
});
</script>
