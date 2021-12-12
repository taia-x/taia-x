<template>
  <TransitionRoot
    appear
    :show="alert.visible"
    as="div"
    enter="transform ease-out duration-300 transition"
    enter-from="translate-x-4 opacity-0"
    enter-to="translate-x-0 opacity-100"
    leave="transform ease-in duration-300 transition"
    leave-from="opacity-100"
    leave-to="opacity-0"
    class="flex items-center p-4 space-x-4 transition-all duration-300 ease-out bg-white border border-gray-300 shadow-xl  rounded-2xl w-96"
  >
    <TransitionChild
      as="div"
      enter="transform ease-out duration-300 transition"
      enter-from="rotate-90 scale-50 opacity-0"
      enter-to="rotate-0 scale-100 opacity-100"
      leave="transform ease-in duration-300 transition"
      leave-from="opacity-100"
      leave-to="opacity-0"
      class="flex self-start"
    >
      <CheckCircleIcon
        v-if="alert.type === 'success'"
        class="w-6 h-6 text-green-300"
      />
      <ExclamationCircleIcon
        v-if="alert.type === 'error'"
        class="w-6 h-6 text-red-500"
      />
      <ExclamationIcon
        v-if="alert.type === 'warning'"
        class="w-6 h-6 text-yellow-300"
      />
      <InformationCircleIcon v-else class="w-6 h-6 text-blue-400" />
    </TransitionChild>
    <TransitionChild
      as="div"
      enter="transform ease-out duration-300 transition"
      enter-from="translate-x-12 opacity-0"
      enter-to="translate-x-0 opacity-100"
      leave="transform ease-in duration-300 transition"
      leave-from="opacity-100"
      leave-to="opacity-0"
      class="flex flex-col w-full"
    >
      <span class="self-start font-medium text-left text-gray-900"
        >{{ alert.type[0].toUpperCase() + alert.type.substring(1) }}!</span
      >
      <span class="font-light text-left text-gray-700">{{
        alert.message
      }}</span>
    </TransitionChild>
    <TransitionChild
      as="button"
      enter="transform ease-out duration-300 transition"
      enter-from="rotate-90 scale-50 opacity-0"
      enter-to="rotate-0 scale-100 opacity-100"
      leave="transform ease-in duration-300 transition"
      leave-from="opacity-100"
      leave-to="opacity-0"
      class="flex self-start"
      @click.prevent="destroyAlert(index)"
    >
      <XIcon
        class="w-6 h-6 text-gray-400 transition duration-150  hover:text-gray-700"
      />
    </TransitionChild>
  </TransitionRoot>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { TransitionRoot, TransitionChild } from "@headlessui/vue";
import {
  CheckCircleIcon,
  ExclamationCircleIcon,
  ExclamationIcon,
  InformationCircleIcon,
  XIcon,
} from "@heroicons/vue/outline";
import { useAlertStore } from "@/stores/useAlerts";
import { Alert } from "@/types";

export default defineComponent({
  components: {
    TransitionRoot,
    TransitionChild,
    CheckCircleIcon,
    ExclamationCircleIcon,
    ExclamationIcon,
    InformationCircleIcon,
    XIcon,
  },
  props: {
    alert: {
      type: Object as PropType<Alert>,
      required: true,
    },
    index: {
      type: Number,
      required: true,
    },
  },
  setup() {
    const { destroyAlert } = useAlertStore();

    return { destroyAlert };
  },
});
</script>
