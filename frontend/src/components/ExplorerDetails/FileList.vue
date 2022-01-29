<template>
  <div
    class="flex items-center justify-between w-full p-2 mt-1 bg-gray-100 rounded-md"
    v-for="file in files"
    :key="file.fileName"
  >
    <div class="flex items-center space-x-2">
      <DocumentTextIcon class="w-5 h-5 text-gray-700" />
      <span class="font-mono truncate">{{ file.fileName }}</span>
    </div>
    <div class="flex items-center space-x-4">
      <span class="font-mono">{{ file.fileSize }} Byte</span>
      <Tooltip
        class="group"
        @click.prevent="fetchPreview(file)"
        v-if="file.previewUri"
      >
        <template #element
          ><EyeIcon
            class="w-5 h-5 text-gray-400 transition-colors duration-150 hover:text-gray-700"
        /></template>
        <template #text>Show Preview</template>
      </Tooltip>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { DocumentTextIcon, EyeIcon } from "@heroicons/vue/outline";
import { ipfsInterface } from "@/services";
import Tooltip from "@/components/Utils/Tooltip.vue";

export default defineComponent({
  components: {
    DocumentTextIcon,
    EyeIcon,
    Tooltip,
  },
  props: {
    files: {
      type: Array,
      required: true,
    },
  },
  setup(_, { emit }) {
    const fetchPreview = async (file) => {
      emit("update:selected", file);
      const asset = await fetch(ipfsInterface.makeGatewayURL(file.previewUri));
      emit("update:code", JSON.stringify(await asset.json(), null, 2));
    };

    return {
      fetchPreview,
    };
  },
});
</script>
