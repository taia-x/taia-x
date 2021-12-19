<template>
  <div>
    <label class="block text-sm font-medium text-gray-700" for="file-upload">
      Dataset
    </label>
    <FileList
      v-if="files.length"
      :files="files"
      @fileRemoved="$emit('fileRemoved', $event)"
    />
    <FileSelect v-else @fileSelected="$emit('filesSelected', $event)" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import FileSelect from "@/components/Utils/FileUpload/FileSelect.vue";
import FileList from "@/components/Utils/FileUpload/FileList.vue";

export default defineComponent({
  components: {
    FileSelect,
    FileList,
  },
  props: {
    files: {
      type: Array,
      required: true,
    },
  },
  emits: ["fileRemoved", "filesSelected"],
});
</script>

<style>
.heroicon-sw-1 path {
  stroke-width: 1.2 !important;
}
</style>
