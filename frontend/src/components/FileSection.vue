<template>
  <div>
    <label class="block text-sm font-medium text-gray-700" for="file-upload">
      Dataset
    </label>
    <FileList
      v-if="fileName"
      :fileName="fileName"
      @fileRemoved="
        fileName = '';
        jsonObject = {};
      "
    />
    <FileSelect v-else @fileSelected="onFileSelected($event)" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import FileSelect from "@/components/FileSelect.vue";
import FileList from "@/components/FileList.vue";

export default defineComponent({
  components: {
    FileSelect,
    FileList,
  },
  setup() {
    const jsonObject = ref({});
    const fileName = ref("");

    const onFileSelected = (e: any): void => {
      const files: FileList = e.target?.files || e.dataTransfer?.files;
      const fileExtension: string = files[0].name.substr(
        files[0].name.indexOf(".")
      );
      if (
        !files[0] ||
        files[0].type !== "application/json" ||
        fileExtension !== ".json"
      )
        return;
      const reader = new FileReader();

      reader.onload = (e: any) => {
        jsonObject.value = JSON.parse(e.target.result);
        fileName.value = files[0].name;
      };

      reader.readAsText(files[0]);
    };

    return { jsonObject, fileName, onFileSelected };
  },
});
</script>

<style>
.heroicon-sw-1 path {
  stroke-width: 1.2 !important;
}
</style>
