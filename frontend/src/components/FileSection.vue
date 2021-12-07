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
    <button
      type="button"
      class="inline-flex justify-center w-full px-4 py-2 mt-3 text-base font-medium text-gray-700 transition duration-200 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
      @click.prevent="saveToIpfs()"
    >
      Save
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import FileSelect from "@/components/FileSelect.vue";
import FileList from "@/components/FileList.vue";
import { ipfsInterface } from "@/services/index";

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
        console.log(jsonObject.value);
      };

      reader.readAsText(files[0]);
    };

    const saveToIpfs = async () => {
      try {
        const uri = await ipfsInterface.writeFile(
          { description: "Test", name: "Testname", data: jsonObject.value },
          "tesla"
        );
      } catch (e) {
        console.log(e);
      }
    };

    return { jsonObject, fileName, onFileSelected, saveToIpfs };
  },
});
</script>

<style>
.heroicon-sw-1 path {
  stroke-width: 1.2 !important;
}
</style>
