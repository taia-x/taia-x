<template>
  <Modal
    :isOpen="isOpen"
    @update:isOpen="$emit('update:isOpen', $event)"
    @close="cancel()"
  >
    <template #title>Create Dataset</template>
    <template #content
      ><div>
        <label for="name" class="block text-sm font-medium text-gray-700">
          Name
        </label>
        <div class="flex w-full mt-1 rounded-md shadow-sm">
          <input
            v-model="name"
            type="text"
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
            v-model="description"
            id="description"
            name="description"
            rows="3"
            class="block w-full mt-1 border border-gray-300 rounded-md shadow-sm  focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
            placeholder="Provide a description of your dataset..."
          />
        </div>
      </div>
      <FileSection
        @filesSelected="onFileSelected($event)"
        @fileRemoved="removeFile($event)"
        :files="files"
    /></template>
    <template #actions>
      <button
        type="button"
        class="inline-flex justify-center w-full px-4 py-2 mt-3 text-base font-medium text-gray-700 transition duration-200 bg-white border border-gray-300 rounded-md shadow-sm  hover:bg-gray-50 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
        @click.prevent="
          $emit('update:isOpen', false);
          cancel();
        "
      >
        Cancel
      </button>
      <button
        type="submit"
        class="inline-flex justify-center px-4 py-2 text-sm font-medium text-white transition duration-200 rounded-md shadow-sm  disabled:cursor-not-allowed disabled:bg-gray-100 disabled:text-gray-400 bg-cyan-500 hover:bg-cyan-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
        @click.prevent="mint()"
        :disabled="!isFormValid"
      >
        Save
      </button>
    </template>
  </Modal>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from "vue";
import FileSection from "@/components/Utils/FileUpload/FileSection.vue";
import Modal from "@/components/Utils/Modal.vue";
import inputFiles from "@/composables/inputFiles";
import { ipfsInterface, tezosInterface } from "@/services";
import { useUserStore } from "@/stores/useUser";
import { useAlertStore } from "@/stores/useAlerts";
import { storeToRefs } from "pinia";

export default defineComponent({
  components: {
    FileSection,
    Modal,
  },
  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },
  },
  setup(_, { emit }) {
    const name = ref("");
    const description = ref("");
    const { files, image, data, onFileSelected, removeFile } = inputFiles();
    const user = useUserStore();
    const alerts = useAlertStore();
    const { address } = storeToRefs(user);

    // firstly writes artifact to ipfs, then writes metadata with link to artifact to ipfs and then mints token
    const mint = async () => {
      try {
        if (address.value) {
          const artifactCid = await ipfsInterface.writeFile(data.value); // artifact to ipfs
          // metadata to ipfs
          const metadataCid = await ipfsInterface.writeFile({
            name: name.value,
            description: description.value,
            artifactUri: artifactCid,
          });
          // mint token via wallet
          await tezosInterface.mintNft({
            operator: "tz1ittpFnVsKxx1M8YPKt7VJEaZfwiBZ6jo7",
            address: address.value,
            price: 1000000,
            metadataUri: metadataCid,
          });
          // closes modal, notifies user and resets values
          emit("update:isOpen", false);
          alerts.createAlert("Successfully minted NFT!", "success");
          cancel();
        } else {
          alerts.createAlert("Login to execute transaction!", "warning");
        }
      } catch (e: any) {
        alerts.createAlert("Something went wrong!", "error");
        throw new Error(e.toString());
      }
    };

    // reset modal inputs
    const cancel = () => {
      name.value = "";
      description.value = "";
      files.value = [];
    };

    // checks if each input field contains values
    const isFormValid = computed(() => {
      return (
        name.value.length > 0 &&
        description.value.length > 0 &&
        files.value.length > 0
      );
    });

    return {
      name,
      description,
      files,
      image,
      data,
      isFormValid,
      cancel,
      onFileSelected,
      removeFile,
      mint,
    };
  },
});
</script>

<style>
.heroicon-sw-1 path {
  stroke-width: 1.2 !important;
}
</style>
