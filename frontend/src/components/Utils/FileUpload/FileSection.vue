<template>
  <div>
    <label class="block text-sm font-medium text-gray-700" for="file-upload">
      Dataset
    </label>
    <FileList
      v-if="files.length"
      :files="files"
      @fileRemoved="$emit('fileRemoved', $event)"
      @ontologyAdded="$emit('ontologyAdded', $event)"
    />
    <input
      id="file"
      name="file-upload"
      type="file"
      accept=".json,.zip"
      v-if="files.length"
      class="sr-only"
      multiple
      @change="$emit('addFiles', $event)"
    />
    <button
      v-if="files.length"
      @click.prevent="openFileSelect"
      class="flex items-center justify-center w-full px-2 py-1 mt-2 ml-auto space-x-2 text-white bg-gray-900 rounded-md h-9 hover:bg-gray-800"
    >
      <PlusIcon class="w-4 h-4" />
      <span>Add Files</span>
    </button>
    <FileSelect v-else @fileSelected="$emit('filesSelected', $event)" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import FileSelect from "@/components/Utils/FileUpload/FileSelect.vue";
import FileList from "@/components/Utils/FileUpload/FileList.vue";
import { PlusIcon } from "@heroicons/vue/solid";

export default defineComponent({
  components: {
    FileSelect,
    FileList,
    PlusIcon,
  },
  props: {
    files: {
      type: Array,
      required: true,
    },
  },
  emits: ["fileRemoved", "filesSelected", "addFiles", "ontologyAdded"],
  methods: {
    openFileSelect() {
      document?.getElementById("file")?.click();
    },
  },
});
</script>

<style>
.heroicon-sw-1 path {
  stroke-width: 1.2 !important;
}
</style>
