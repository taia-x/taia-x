<template>
  <div>
    <label :for="name" class="block text-sm font-medium text-gray-700">
      <slot name="title"></slot>
    </label>
    <div class="flex items-center">
      <div class="flex w-full mt-1">
        <input
          v-if="element === 'input'"
          v-model="input"
          tabindex="1"
          autofocus
          :type="type"
          :name="name"
          :id="name"
          class="flex-1 block w-full placeholder-gray-300 border-gray-100 focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
          :class="
            element === 'input' && type === 'number'
              ? 'border-l-2 border-t-2 border-b-2 border-r-0 rounded-l-md'
              : 'border-2 rounded-md'
          "
          :placeholder="placeholder"
          @change="$emit('update', input)"
        />

        <textarea
          v-else
          v-model="input"
          tabindex="1"
          :type="type"
          :name="name"
          :id="name"
          :rows="rows"
          class="flex-1 block w-full placeholder-gray-300 border-2 border-gray-100 rounded-md focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
          :placeholder="placeholder"
          @change="$emit('update', input)"
        />
      </div>
      <div
        v-if="element === 'input' && type === 'number'"
        class="flex-1 block px-6 py-2 mt-1 text-gray-700 bg-gray-100 border-2 border-gray-100 sm:text-sm rounded-r-md"
      >
        ꜩ
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, watchEffect } from "vue";

export default defineComponent({
  props: {
    type: {
      type: String,
      default: "text",
    },
    placeholder: {
      type: String,
      required: true,
    },
    rows: {
      type: String,
      default: "1",
    },
    name: {
      type: String,
      required: true,
    },
    element: {
      type: String,
      default: "input",
    },
    value: {
      type: [String, Number],
      required: true,
    },
  },
  setup(props) {
    const input = ref("");

    watchEffect(() => {
      if (!props.value) input.value = "";
    });

    return { input };
  },
});
</script>
