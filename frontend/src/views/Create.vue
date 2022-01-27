<template>
  <h1
    class="pt-10 text-2xl font-extrabold tracking-tight text-gray-900 sm:text-3xl"
  >
    Create Dataset
  </h1>
  <form class="mt-16">
    <div class="sm:rounded-md">
      <div class="space-y-6 bg-white">
        <FileSection
          @filesSelected="onFileSelected($event)"
          @addFiles="onFileSelected($event)"
          @fileRemoved="removeFile($event)"
          @ontologyAdded="ontologies[$event.fileName] = $event"
          :files="files"
        />
        <NameInput @update:name="name = $event" />
        <DescriptionInput @update:description="description = $event" />
        <TagsInput @update:tags="tags = $event" />
      </div>
      <div class="w-full mt-6 space-x-2 text-right">
        <button
          type="button"
          class="inline-flex justify-center w-full px-4 py-2 mt-3 text-base font-medium text-gray-700 transition duration-200 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
          tabindex="5"
          @click.prevent="
            reset();
            $router.push('/explore');
          "
        >
          Cancel
        </button>
        <button
          type="submit"
          tabindex="4"
          class="inline-flex justify-center px-4 py-2 text-sm font-medium text-white transition duration-200 rounded-md shadow-sm disabled:cursor-not-allowed disabled:bg-gray-100 disabled:text-gray-400 bg-cyan-500 hover:bg-cyan-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
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
import NameInput from "@/components/Create/NameInput.vue";
import DescriptionInput from "@/components/Create/DescriptionInput.vue";
import TagsInput from "@/components/Create/TagsInput.vue";
import inputFiles from "@/composables/inputFiles";
import { ipfsInterface, tezosInterface } from "@/services";
import { useUserStore } from "@/stores/useUser";
import { useAlertStore } from "@/stores/useAlerts";
import { storeToRefs } from "pinia";
import { TokenMetadata } from "@/types";

export default defineComponent({
  components: {
    FileSection,
    NameInput,
    DescriptionInput,
    TagsInput,
  },
  setup() {
    const name = ref("");
    const tags = ref("");
    const description = ref("");
    const ontologies = ref({} as any);
    const { files, archive, generateSHA256, onFileSelected, removeFile } =
      inputFiles();
    const user = useUserStore();
    const alerts = useAlertStore();
    const { address } = storeToRefs(user);

    // reset modal inputs
    const reset = () => {
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

    // upload artifact to backend, upload ontologies on ipfs, upload metadata on ipfs, mint token
    const mint = async () => {
      try {
        // create form data to upload file via post request
        const form = new FormData();
        form.append("archive", archive.value);

        // upload file
        const uploadResponse = await fetch("http://localhost:8000/upload", {
          method: "POST",
          body: form,
        });
        const { artifactUri }: { artifactUri: string } =
          await uploadResponse.json();
        // const boy: any = {
        //   nft_id: "1",
        //   sig: "Test",
        //   pbkey: "Test",
        // };
        // const res2 = await fetch(artifactUri, {
        //   method: "POST",
        //   headers: { "Content-Type": "application/json" },
        //   body: JSON.stringify(boy),
        // });
        // console.log(
        //   "cool2 ",
        //   await generateSHA256(new Blob([await res2.arrayBuffer()]))
        // );

        // generate hash from zip archive
        const hash = await generateSHA256(files.value[0]);

        // store artifactUri in formats for token metadata file
        const formats = [
          {
            uri: artifactUri,
            hash: `sha256://${hash}`,
            mimeType: "application/zip",
          },
        ];

        // if ontolofies were uploaded, add format for each ontology file including uri, hash and mimetype
        Object.keys(ontologies.value).forEach((key) =>
          formats.push({
            uri: ontologies.value[key]?.fileUri,
            hash: ontologies.value[key]?.fileHash,
            mimeType: "application/json",
          } as any)
        );

        // construct token metadata to be uploaded to ipfs
        const tokenMetadata: TokenMetadata = {
          name: name.value,
          description: description.value,
          tags: tags.value.length
            ? tags.value.replace(/ /g, "").split(/[,]+/)
            : [],
          files: files.value.map((file: File) => ({
            fileName: file.name,
            fileSize: file.size,
            mimeType: file.type,
            ontologyUri: ontologies.value[file.name]?.fileUri || null,
          })),
          formats,
          artifactUri,
        };
        const metadataUri = await ipfsInterface.writeFile(tokenMetadata); // upload metadata to ipfs

        // mint token
        await tezosInterface.mintNft({
          hash,
          operator: "tz1ittpFnVsKxx1M8YPKt7VJEaZfwiBZ6jo7",
          address: address.value,
          price: 1000000,
          metadataUri,
        });

        // notifies user and resets values
        alerts.createAlert("Successfully minted NFT!", "success");
        reset();
      } catch (e: any) {
        alerts.createAlert("Something went wrong!", "error");
        throw new Error(e.toString());
      }
    };

    return {
      name,
      description,
      ontologies,
      files,
      isFormValid,
      reset,
      onFileSelected,
      removeFile,
      tags,
      mint,
    };
  },
});
</script>
