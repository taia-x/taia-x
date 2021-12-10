<template>
  <TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="$emit('update:isOpen', false)">
      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div class="min-h-screen px-4 text-center">
          <TransitionChild
            as="template"
            enter="duration-300 ease-out"
            enter-from="opacity-0"
            enter-to="opacity-100"
            leave="duration-200 ease-in"
            leave-from="opacity-100"
            leave-to="opacity-0"
          >
            <DialogOverlay class="fixed inset-0 bg-black bg-opacity-30" />
          </TransitionChild>

          <span class="inline-block h-screen align-middle" aria-hidden="true">
            &#8203;
          </span>

          <TransitionChild
            as="template"
            enter="delay-100 duration-300 ease-out"
            enter-from="opacity-0 scale-95"
            enter-to="opacity-100 scale-100"
            leave="delay-100 duration-200 ease-in"
            leave-from="opacity-100 scale-100"
            leave-to="opacity-0 scale-95"
          >
            <div
              class="inline-block w-full max-w-3xl p-6 my-8 overflow-hidden text-left align-middle transition-all transform bg-white shadow-xl  rounded-2xl"
            >
              <DialogTitle
                as="h3"
                class="text-lg font-medium leading-6 text-gray-900"
              >
                Create Dataset
              </DialogTitle>
              <div class="mt-8">
                <form action="#" method="POST">
                  <div class="sm:rounded-md">
                    <div class="space-y-6 bg-white">
                      <div>
                        <label
                          for="name"
                          class="block text-sm font-medium text-gray-700"
                        >
                          Name
                        </label>
                        <div class="flex w-full mt-1 rounded-md shadow-sm">
                          <input
                            type="text"
                            v-model="name"
                            name="name"
                            id="name"
                            class="flex-1 block w-full border-gray-300 rounded-md  focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
                            placeholder="Dataset name"
                          />
                        </div>
                      </div>

                      <div>
                        <label
                          for="description"
                          class="block text-sm font-medium text-gray-700"
                        >
                          Description
                        </label>
                        <div class="mt-1">
                          <textarea
                            id="description"
                            name="description"
                            v-model="description"
                            rows="3"
                            class="block w-full mt-1 border border-gray-300 rounded-md shadow-sm  focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
                            placeholder="Provide a description of your dataset..."
                          />
                        </div>
                      </div>
                      <FileSection @filesSelected="onFileSelected($event)" />
                    </div>
                    <div class="w-full mt-6 space-x-2 text-right">
                      <button
                        type="button"
                        class="inline-flex justify-center w-full px-4 py-2 mt-3 text-base font-medium text-gray-700 transition duration-200 bg-white border border-gray-300 rounded-md shadow-sm  hover:bg-gray-50 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
                        @click.prevent="$emit('update:isOpen', false)"
                      >
                        Cancel
                      </button>
                      <button
                        type="submit"
                        class="inline-flex justify-center px-4 py-2 text-sm font-medium text-white transition duration-200 rounded-md shadow-sm  bg-cyan-500 hover:bg-cyan-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
                        @click.prevent="writeToIpfs()"
                      >
                        Save
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import {
  Dialog,
  DialogOverlay,
  DialogTitle,
  TransitionRoot,
  TransitionChild,
} from "@headlessui/vue";
import FileSection from "@/components/FileSection.vue";
import { ipfsInterface } from "@/services";
import { useOntologiesStore } from "@/stores/useOntologies";

export default defineComponent({
  components: {
    Dialog,
    DialogOverlay,
    DialogTitle,
    TransitionRoot,
    TransitionChild,
    FileSection,
  },
  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },
  },
  setup() {
    const name = ref("");
    const description = ref("");
    const files = ref([]);
    const image = ref("");
    const data = ref("");
    const ontologies = useOntologiesStore();

    const dataReader = new FileReader();
    const imageReader = new FileReader();

    dataReader.onload = (e: any) => {
      data.value = JSON.parse(e.target.result);
    };

    imageReader.onload = (e: any) => {
      image.value = e.target.result;
    };

    const onFileSelected = (e: any): void => {
      const files: FileList = e.target?.files || e.dataTransfer?.files;
      Object.entries(files).forEach(([key, value], index) => {
        const file: File = files[index];
        const fileExtension: string = file.name.substr(file.name.indexOf("."));
        if (file.type === "application/json" && fileExtension === ".json") {
          dataReader.readAsText(file);
        }
        if (file.type === "image/png" && fileExtension === ".png") {
          imageReader.readAsArrayBuffer(file);
        }
      });
    };

    const writeToIpfs = async () => {
      const metadata = {
        name: name.value,
        description: description.value,
      };
      try {
        const asset = await ipfsInterface.writeFile(data.value);
        if (asset?.assetURI) {
          const data = await ipfsInterface.writeFile({
            ...metadata,
            assetUri: asset.assetURI,
          });
          const dataa = await fetch(data.metadataGatewayURL);
          const ontology = await dataa.json();
          ontologies.$patch((state) => (state.ont = [...state.ont, ontology]));
        }
      } catch (e) {
        throw new Error("Unable to write to IPFS!");
      }
    };

    return { name, description, files, writeToIpfs, onFileSelected };
  },
});
</script>

<style>
.heroicon-sw-1 path {
  stroke-width: 1.2 !important;
}
</style>
