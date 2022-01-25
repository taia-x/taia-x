<template>
  <Popover v-if="address" class="relative" v-slot="{ open }">
    <PopoverButton
      class="relative flex items-center justify-center pl-3 font-semibold text-gray-500 transition duration-200 ease-in-out transform rounded-md text-md hover:text-cyan-500 group"
    >
      <img
        :src="`${ACCOUNT_IMAGE_PATH}${address}`"
        class="absolute left-0 w-10 h-10"
      />
      <span class="ml-9">
        {{ privateAddress }}
      </span>
      <ChevronDownIcon
        class="w-5 h-5 text-gray-900 transition-transform duration-300 transform translate-x-1"
        :class="open ? '-rotate-180' : '-rotate-0'"
      />
    </PopoverButton>

    <transition
      enter-active-class="transition duration-100 ease-out"
      enter-from-class="transform scale-95 opacity-0"
      enter-to-class="transform scale-100 opacity-100"
      leave-active-class="transition duration-75 ease-out"
      leave-from-class="transform scale-100 opacity-100"
      leave-to-class="transform scale-95 opacity-0"
    >
      <PopoverPanel
        class="absolute right-0 z-10 flex flex-col mt-4 bg-white border-2 border-gray-100 rounded-md"
      >
        <UserMenuContent :address="address" :privateAddress="privateAddress" />
      </PopoverPanel>
    </transition>
  </Popover>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import UserMenuContent from "@/components/Header/UserMenu/UserMenuContent.vue";
import { ChevronDownIcon } from "@heroicons/vue/solid";
import { Popover, PopoverButton, PopoverPanel } from "@headlessui/vue";
import { ACCOUNT_IMAGE_PATH } from "@/constants";

export default defineComponent({
  components: {
    UserMenuContent,
    ChevronDownIcon,
    Popover,
    PopoverButton,
    PopoverPanel,
  },
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
  setup() {
    return { ACCOUNT_IMAGE_PATH };
  },
});
</script>
