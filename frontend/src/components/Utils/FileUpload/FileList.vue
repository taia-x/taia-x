<template>
  <div
    class="flex items-center justify-between w-full h-12 p-2 mt-2 rounded-md bg-gray-50"
    v-for="(file, index) in files"
    :key="file.name"
    :index="index"
  >
    <div class="flex items-center space-x-2">
      <DocumentTextIcon class="w-5 h-5 text-gray-700" />
      <span class="font-mono text-sm truncate">{{ file.name }}</span>
    </div>
    <div class="flex items-center py-1 space-x-4">
      <input
        id="preview"
        name="file-upload"
        type="file"
        accept=".json"
        v-if="files.length"
        class="sr-only"
        @change="uploadPreview($event)"
      />
      <button
        @click.prevent="openFileSelect"
        v-if="!previews[file.name]"
        class="px-2 py-1 space-x-2 text-xs text-white transition-colors duration-100 bg-gray-900 rounded-md hover:bg-gray-800"
      >
        Add Preview
      </button>
      <button
        @click.prevent="delete previews[file.name]"
        v-if="previews[file.name]"
        class="px-2 py-1 space-x-2 text-xs text-white transition-colors duration-100 bg-red-500 rounded-md hover:bg-red-400"
      >
        Remove Preview
      </button>
      <XIcon
        class="w-5 h-5 text-gray-400 cursor-pointer hover:text-gray-700"
        @click.prevent="$emit('fileRemoved', index)"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { DocumentTextIcon } from "@heroicons/vue/outline";
import { XIcon } from "@heroicons/vue/solid";
import { ipfsInterface } from "@/services";
import inputFiles from "@/composables/inputFiles";

export default defineComponent({
  components: {
    DocumentTextIcon,
    XIcon,
  },
  props: {
    files: {
      type: Array,
      required: true,
    },
    previews: {
      type: Object,
      required: true,
    },
  },
  emits: ["fileRemoved", "previewAdded"],
  setup(_, { emit }) {
    const { generateSHA256 } = inputFiles();

    const openFileSelect = () => {
      document?.getElementById("preview")?.click();
    };

    const uploadPreview = async (e: any) => {
      const files: any = e?.target?.files
        ? Array.from(e.target.files)
        : Array.from(e.dataTransfer.files);
      try {
        const previewCid = await ipfsInterface.writeFile(files[0]);
        const preview = {
          fileName: files[0].name,
          fileUri: previewCid,
          fileHash: `sha256://${await generateSHA256(files[0])}`,
        };
        emit("previewAdded", preview);
      } catch (e: any) {
        throw new Error(e.toString());
      }
    };

    return { openFileSelect, uploadPreview };
  },
});
</script>
