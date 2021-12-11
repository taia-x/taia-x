<template>
  <Popover v-if="address" class="relative" v-slot="{ open }">
    <PopoverButton
      class="flex items-center justify-center px-3 py-2 font-semibold text-gray-500 transition duration-300 ease-in-out transform bg-gray-100 rounded-md  text-md hover:text-gray-900 group"
    >
      <span>
        {{ privateAddress }}
      </span>
      <ChevronDownIcon
        class="w-5 h-5 transition-transform duration-300 transform translate-x-1 "
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
        class="absolute right-0 z-10 flex flex-col w-screen max-w-xs p-4 px-4 mt-1 bg-white border border-gray-200 rounded-lg shadow-md  bg-opacity-80 backdrop-filter backdrop-blur"
      >
        <AccountToggleContent
          :address="address"
          :privateAddress="privateAddress"
          :balance="balance"
        />
      </PopoverPanel>
    </transition>
  </Popover>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AccountToggleContent from "@/components/Header/Account/AccountToggleContent.vue";
import { ChevronDownIcon } from "@heroicons/vue/solid";
import { Popover, PopoverButton, PopoverPanel } from "@headlessui/vue";

export default defineComponent({
  components: {
    AccountToggleContent,
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
    balance: {
      type: Number,
      required: true,
    },
  },
});
</script>
