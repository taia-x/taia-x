<template>
  <div
    class="flex items-center justify-between w-full p-2 mt-2 rounded-md bg-gray-50"
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
        id="ontology"
        name="file-upload"
        type="file"
        accept=".json"
        v-if="files.length"
        class="sr-only"
        @change="uploadOntology($event)"
      />
      <button
        v-if="files.length"
        @click.prevent="openFileSelect"
        class="px-2 py-1 space-x-2 text-xs text-white transition-colors duration-100 bg-gray-900 rounded-md bg-opacity-10 hover:bg-gray-800"
      >
        Add Ontology
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
  },
  emits: ["fileRemoved", "ontologyAdded"],
  setup(_, { emit }) {
    const { generateSHA256 } = inputFiles();

    const openFileSelect = () => {
      document?.getElementById("ontology")?.click();
    };

    const uploadOntology = async (e: any) => {
      const files: any = e?.target?.files
        ? Array.from(e.target.files)
        : Array.from(e.dataTransfer.files);
      try {
        const ontologyCid = await ipfsInterface.writeFile(files[0]);
        const ontology = {
          fileName: files[0].name,
          fileUri: ontologyCid,
          fileHash: `sha256://${await generateSHA256(files[0])}`,
        };
        emit("ontologyAdded", ontology);
      } catch (e: any) {
        throw new Error(e.toString());
      }
    };

    return { openFileSelect, uploadOntology };
  },
});
</script>
