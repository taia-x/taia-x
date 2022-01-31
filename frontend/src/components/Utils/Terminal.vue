<template>
  <div class="relative flex overflow-hidden bg-cyan-500 md:rounded-xl h-96">
    <div class="absolute inset-0 bg-black bg-opacity-75"></div>
    <div class="relative flex flex-col w-full">
      <div class="flex items-center flex-none px-4 h-11">
        <div class="flex space-x-1.5">
          <div class="w-3 h-3 border-2 border-red-500 rounded-full"></div>
          <div class="w-3 h-3 border-2 rounded-full border-amber-400"></div>
          <div class="w-3 h-3 border-2 border-green-400 rounded-full"></div>
        </div>
        <span
          class="mx-auto text-sm text-white transform -translate-x-5 text-opacity-30"
          >{{ hasPreview ? file.fileName : "" }}</span
        >
      </div>
      <div
        class="relative flex flex-col flex-auto min-h-0 border-t border-white border-opacity-10"
      >
        <div
          class="absolute inset-y-0 left-0 hidden bg-black bg-opacity-25 md:block"
          style="width: 50px"
        ></div>
        <div class="flex flex-auto w-full min-h-0 overflow-auto">
          <div class="relative flex-auto w-full">
            <Code :code="code" v-if="code" />
            <div v-else class="flex h-full">
              <div style="width: 50px"></div>
              <div class="flex items-center justify-center h-full mx-auto">
                <div
                  v-if="!hasPreview"
                  class="text-white transform -translate-x-5 text-opacity-30"
                >
                  No Preview available
                </div>
                <LoadingSpinner :size="8" v-else />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from "vue";
import Code from "@/components/Utils/Code.vue";
import LoadingSpinner from "@/components/Utils/LoadingSpinner.vue";

export default defineComponent({
  components: {
    Code,
    LoadingSpinner,
  },
  props: {
    code: {
      type: String,
      required: true,
    },
    file: {
      type: Object,
      required: true,
    },
    token: {
      type: [Object, null],
      required: true,
    },
  },
  setup(props) {
    const hasPreview = computed(() => {
      if (props.token) {
        return props.token.files.some((file) => file.previewUri);
      }
      return true;
    });

    return { hasPreview };
  },
});
</script>
