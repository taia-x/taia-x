<template>
  <div
    class="flex items-center justify-between w-full p-2 mt-1 bg-gray-100 rounded-md"
    v-for="download in Object.keys(downloads)"
    :key="download"
  >
    <div class="flex items-center space-x-2">
      <DocumentTextIcon class="w-5 h-5 text-gray-700" />
      <span class="font-mono truncate">{{ downloads[download].name }}</span>
    </div>
    <div class="flex items-center space-x-4">
      <Tooltip class="group">
        <template #element
          ><span class="relative flex w-3 h-3">
            <span
              class="absolute inline-flex w-full h-full rounded-full opacity-75 animate-ping"
              :class="
                downloads[download].verified ? 'bg-green-400' : 'bg-red-500'
              "
            ></span>
            <span
              class="relative inline-flex w-3 h-3 rounded-full"
              :class="
                downloads[download].verified ? 'bg-green-500' : 'bg-red-500'
              "
            ></span> </span
        ></template>
        <template #text>{{
          downloads[download].verified ? "Verified" : "File manipulated"
        }}</template>
      </Tooltip>
      <Tooltip
        class="mr-1 group"
        @click.prevent="downloadZip(downloads[download])"
      >
        <template #element
          ><DownloadIcon
            class="w-6 h-6 text-gray-400 transition-colors duration-150 hover:text-gray-700"
        /></template>
        <template #text>Download</template>
      </Tooltip>
    </div>
  </div>
</template>

<script>
import { defineComponent, watch, reactive } from "vue";
import { useRoute } from "vue-router";
import { getPurchases } from "@/services/graphql/queries";
import { useQuery, useResult } from "@vue/apollo-composable";
import { DocumentTextIcon, DownloadIcon } from "@heroicons/vue/outline";
import Tooltip from "@/components/Utils/Tooltip.vue";
import inputFiles from "@/composables/inputFiles";
import { saveAs } from "file-saver";

export default defineComponent({
  components: {
    DocumentTextIcon,
    DownloadIcon,
    Tooltip,
  },
  setup() {
    const route = useRoute();
    const { generateSHA256 } = inputFiles();
    const downloads = reactive({});

    const { result, loading, refetch } = useQuery(
      getPurchases,
      () => ({
        address: route.params.address,
      }),
      {
        fetchPolicy: "cache-and-network",
      }
    );

    const tokens = useResult(
      result,
      null,
      ({ account_by_pk }) => account_by_pk.purchases
    );

    watch(tokens, () => {
      tokens.value.forEach(async (token) => {
        const artifact = await fetch(token.artifact_uri, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            nft_id: 1,
            sig: "hi",
            pbkey: "test",
          }),
        });
        const artifactBlob = await artifact.blob();
        downloads[token.id] = {
          artifact: artifactBlob,
          verified: token.hash === (await generateSHA256(artifactBlob)),
          name: token.name,
        };
      });
    });

    const downloadZip = async (download) => {
      saveAs(download.artifact, "Archive.zip");
    };

    watch(route, () => {
      if (route.name === "downloads") refetch();
    });

    return {
      route,
      loading,
      downloads,
      downloadZip,
    };
  },
});
</script>
