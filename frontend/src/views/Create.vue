<template>
  <h1
    class="pt-10 text-2xl font-extrabold tracking-tight text-gray-900  sm:text-3xl"
  >
    Create Dataset
  </h1>
  <form class="mt-16">
    <div class="sm:rounded-md">
      <div class="space-y-6 bg-white">
        <FileSection
          @filesSelected="onFileSelected($event)"
          @fileRemoved="removeFile($event)"
          :files="files"
        />
        <div>
          <label for="name" class="block text-sm font-medium text-gray-700">
            Name
          </label>
          <div class="flex w-full mt-1 rounded-md shadow-sm">
            <input
              v-model="name"
              tabindex="1"
              autofocus
              type="text"
              name="name"
              id="name"
              class="flex-1 block w-full border-gray-300 rounded-md  focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
              placeholder="Dataset name"
            />
          </div>
        </div>
        <div>
          <label for="name" class="block text-sm font-medium text-gray-700">
            Tags
          </label>
          <div class="flex w-full mt-1 rounded-md shadow-sm">
            <input
              v-model="name"
              tabindex="1"
              autofocus
              type="text"
              name="name"
              id="name"
              class="flex-1 block w-full border-gray-300 rounded-md  focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
              placeholder="Comma separated list"
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
              tabindex="2"
              id="description"
              name="description"
              rows="6"
              class="block w-full mt-1 border border-gray-300 rounded-md shadow-sm  focus:ring-cyan-500 focus:border-cyan-500 sm:text-sm"
              placeholder="Provide a description of your dataset..."
            />
          </div>
        </div>
      </div>
      <div class="w-full pt-6">
        <div class="w-full mx-auto bg-white rounded-2xl">
          <Disclosure v-slot="{ open }">
            <DisclosureButton
              class="flex justify-between w-full py-4 text-sm font-medium text-left text-gray-700 bg-white rounded-lg  group hover:bg-gray-100 focus:outline-none focus-visible:ring focus-visible:ring-cyan-500 focus-visible:ring-opacity-75"
            >
              <span
                class="transition-all duration-200 transform  group-hover:translate-x-4"
                >Attributes</span
              >
              <ChevronUpIcon
                :class="open ? 'transform rotate-0' : 'transform rotate-180'"
                class="w-5 h-5 text-gray-700 transition duration-200 ease-in-out transform  group-hover:-translate-x-4"
              />
            </DisclosureButton>
            <DisclosurePanel class="px-4 pt-4 pb-2 text-sm text-gray-500">
              If you're unhappy with your purchase for any reason, email us
              within 90 days and we'll refund you in full, no questions asked.
            </DisclosurePanel>
          </Disclosure>
          <Disclosure as="div" class="mt-2" v-slot="{ open }">
            <DisclosureButton
              class="flex justify-between w-full py-4 text-sm font-medium text-left text-gray-700 bg-white rounded-lg  group hover:bg-gray-100 focus:outline-none focus-visible:ring focus-visible:ring-cyan-500 focus-visible:ring-opacity-75"
            >
              <span
                class="transition-all duration-200 transform  group-hover:translate-x-4"
                >Levels</span
              >
              <ChevronUpIcon
                :class="open ? 'transform rotate-0' : 'transform rotate-180'"
                class="w-5 h-5 text-gray-700 transition duration-200 ease-in-out transform  group-hover:-translate-x-4"
              />
            </DisclosureButton>
            <DisclosurePanel class="px-4 pt-4 pb-2 text-sm text-gray-500">
              No.
            </DisclosurePanel>
          </Disclosure>
          <Disclosure as="div" class="mt-2" v-slot="{ open }">
            <DisclosureButton
              class="flex justify-between w-full py-4 text-sm font-medium text-left text-gray-700 bg-white rounded-lg  hover:bg-gray-100 focus:outline-none focus-visible:ring focus-visible:ring-cyan-500 focus-visible:ring-opacity-75"
            >
              <span>Stats</span>
              <ChevronUpIcon
                :class="open ? 'transform rotate-0' : 'transform rotate-180'"
                class="w-5 h-5 text-gray-700 transition duration-200 ease-in-out "
              />
            </DisclosureButton>
            <DisclosurePanel class="px-4 pt-4 pb-2 text-sm text-gray-500">
              No.
            </DisclosurePanel>
          </Disclosure>
        </div>
      </div>
      <div class="w-full mt-6 space-x-2 text-right">
        <button
          type="button"
          class="inline-flex justify-center w-full px-4 py-2 mt-3 text-base font-medium text-gray-700 transition duration-200 bg-white border border-gray-300 rounded-md shadow-sm  hover:bg-gray-50 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
          tabindex="4"
          @click.prevent="
            cancel();
            $router.push('/explore');
          "
        >
          Cancel
        </button>
        <button
          type="submit"
          tabindex="3"
          class="inline-flex justify-center px-4 py-2 text-sm font-medium text-white transition duration-200 rounded-md shadow-sm  disabled:cursor-not-allowed disabled:bg-gray-100 disabled:text-gray-400 bg-cyan-500 hover:bg-cyan-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
          @click.prevent="mint()"
          :disabled="!isFormValid"
        >
          Save
        </button>
      </div>
    </div>
  </form>
</template>

<script lang="ts">
import { computed, defineComponent, ref } from "vue";
import FileSection from "@/components/Utils/FileUpload/FileSection.vue";
import inputFiles from "@/composables/inputFiles";
import { Disclosure, DisclosureButton, DisclosurePanel } from "@headlessui/vue";
import { ChevronUpIcon } from "@heroicons/vue/solid";
import { ipfsInterface, tezosInterface } from "@/services";
import { useUserStore } from "@/stores/useUser";
import { useAlertStore } from "@/stores/useAlerts";
import { storeToRefs } from "pinia";

export default defineComponent({
  components: {
    FileSection,
    ChevronUpIcon,
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
  },
  setup(_, { emit }) {
    const name = ref("");
    const description = ref("");
    const { files, image, data, onFileSelected, removeFile } = inputFiles();
    const user = useUserStore();
    const alerts = useAlertStore();
    const { address } = storeToRefs(user);

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