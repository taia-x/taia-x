<template>
  <div
    class="relative cursor-pointer"
    @mouseover="isHidden = false"
    @mouseleave="isHidden = true"
  >
    <slot name="element"></slot>
    <span
      class="absolute inset-x-0 bottom-full mb-2.5 justify-center whitespace-nowrap"
      :class="isHidden ? 'hidden' : 'flex'"
    >
      <span
        class="px-3 py-1 text-xs font-medium text-white bg-gray-900 rounded-md filter drop-shadow-md"
      >
        <svg
          aria-hidden="true"
          width="16"
          height="6"
          viewBox="0 0 16 6"
          class="absolute -mt-px -ml-2 text-gray-900 left-1/2 top-full"
        >
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M15 0H1V1.00366V1.00366V1.00371H1.01672C2.72058 1.0147 4.24225 2.74704 5.42685 4.72928C6.42941 6.40691 9.57154 6.4069 10.5741 4.72926C11.7587 2.74703 13.2803 1.0147 14.9841 1.00371H15V0Z"
            fill="currentColor"
          ></path>
        </svg>
        <slot name="text"></slot>
      </span>
    </span>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const isHidden = ref(true);

    return {
      isHidden,
    };
  },
});
</script>
