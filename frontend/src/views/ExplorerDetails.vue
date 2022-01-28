<template>
  <Terminal
    :code="code"
    :file="selected"
    :token="token"
    class="mt-10 filter drop-shadow-2xl"
  />
  <div class="flex items-center justify-between pt-10 pb-4">
    <div v-if="token && token.files">
      <h1 class="text-3xl font-extrabold tracking-tight text-gray-800">
        {{ token?.name }}
      </h1>
      <div class="flex items-center mt-1 space-x-4 text-xl text-gray-400">
        <div># {{ route.params.id }}</div>
        <div class="flex items-center space-x-1">
          <DocumentIcon class="w-5 h-5" />
          <span>{{ token?.files.length }} Files</span>
        </div>
        <div class="flex items-center space-x-1">
          <ClockIcon class="w-5 h-5" />
          <span>30s</span>
        </div>
      </div>
    </div>
    <a
      v-if="token && token.creator_id"
      :href="`https://tzkt.io/${token?.creator_id}`"
      target="_blank"
      class="z-10 flex items-center space-x-2"
    >
      <div class="flex flex-col">
        <div class="font-medium text-right text-gray-700">Owner</div>
        <div class="pb-2 text-sm font-medium text-right text-gray-400">
          {{ getPrivatizedAddress(token?.creator_id) }}
        </div>
      </div>
      <img
        :src="`https://services.tzkt.io/v1/avatars/${token?.creator_id}`"
        class="w-16 h-16 my-auto"
      />
    </a>
  </div>
  <button
    @click.prevent="buyToken"
    v-if="token && token.price"
    class="flex items-center px-3 text-white transition duration-300 ease-in-out transform border-2 border-b-4 rounded-md h-10 bg-cyan-500 hover:bg-cyan-600 text-md whitespace-nowrap border-cyan-700 hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
  >
    Buy for {{ token.price / 1000000 }} ꜩ
  </button>
  <div class="flex flex-col pt-12 pb-20 space-y-12">
    <div class="space-y-4">
      <h3
        class="flex items-center space-x-1 text-xl font-semibold text-gray-900"
      >
        <span>Description</span>
        <InformationCircleIcon
          class="w-5 h-5 text-gray-400 transform -translate-y-1"
        />
      </h3>
      <p class="text-base text-gray-700">
        {{ token?.description }}
      </p>
    </div>
    <div class="space-y-4">
      <h3
        class="flex items-center space-x-1 text-xl font-semibold text-gray-900"
      >
        <span>Attributes</span>
        <InformationCircleIcon
          class="w-5 h-5 text-gray-400 transform -translate-y-1"
        />
      </h3>
      <p class="text-base text-gray-700">
        {{ token?.description }}
      </p>
    </div>
    <div class="space-y-4" v-if="token && token.files">
      <h3
        class="flex items-center space-x-1 text-xl font-semibold text-gray-900"
      >
        <span>Files</span>
        <InformationCircleIcon
          class="w-5 h-5 text-gray-400 transform -translate-y-1"
        />
      </h3>
      <div
        class="flex items-center justify-between w-full p-2 mt-1 bg-gray-100 rounded-md"
        v-for="file in token.files"
        :key="file.fileName"
      >
        <div class="flex items-center space-x-2">
          <DocumentTextIcon class="w-5 h-5 text-gray-700" />
          <span class="font-mono truncate">{{ file.fileName }}</span>
        </div>
        <div class="flex items-center space-x-4">
          <span class="font-mono">{{ file.fileSize }} Byte</span>
          <Tooltip
            class="group"
            @click.prevent="fetchPreview(file)"
            v-if="file.previewUri"
          >
            <template #element
              ><EyeIcon
                class="w-5 h-5 text-gray-400 transition-colors duration-150 hover:text-gray-700"
            /></template>
            <template #text>Show Preview</template>
          </Tooltip>
        </div>
      </div>
    </div>
    <div v-if="token">
      <History :token="token" />
    </div>
  </div>
</template>

<script>
import { defineComponent, watchEffect, ref } from "vue";
import Terminal from "@/components/Utils/Terminal.vue";
import History from "@/components/History/History.vue";
import { useRoute } from "vue-router";
import {
  ClockIcon,
  DocumentIcon,
  InformationCircleIcon,
  DocumentTextIcon,
  EyeIcon,
} from "@heroicons/vue/outline";
import { highlightAll } from "prismjs";
import { ipfsInterface, tezosInterface } from "@/services";
import { useQuery, useResult } from "@vue/apollo-composable";
import { getSingleTokenMetadata } from "@/services/graphql/queries";
import Tooltip from "@/components/Utils/Tooltip.vue";
import { useAlertStore } from "@/stores/useAlerts";

export default defineComponent({
  components: {
    Terminal,
    ClockIcon,
    DocumentIcon,
    InformationCircleIcon,
    DocumentTextIcon,
    EyeIcon,
    Tooltip,
    History,
  },
  setup() {
    const route = useRoute();
    const alerts = useAlertStore();
    const code = ref("");
    const token = ref(null);
    const selected = ref({});

    // fetches single token metadata based on route param
    const { result } = useQuery(getSingleTokenMetadata, () => ({
      id: Number(route.params.id),
    }));

    // gets token metadata when result is loaded
    const token_metadata = useResult(
      result,
      null,
      ({ token_by_pk }) => token_by_pk
    );

    // render ui when token_metadata contains values
    watchEffect(async () => {
      if (token_metadata?.value?.id) {
        selected.value = token_metadata.value.files[0];
        token.value = token_metadata.value;
        if (token_metadata.value.files) {
          const file = token_metadata.value.files.find(
            (file) => file.previewUri !== null
          );
          if (file) {
            const asset = await fetch(
              ipfsInterface.makeGatewayURL(file.previewUri)
            );
            code.value = JSON.stringify(await asset.json(), null, 2);
          }
        }
      }
    });

    const fetchPreview = async (file) => {
      if (
        file.previewUri !== null &&
        selected.value.fileName !== file.fileName
      ) {
        selected.value = file;
        const asset = await fetch(
          ipfsInterface.makeGatewayURL(file.previewUri)
        );
        code.value = JSON.stringify(await asset.json(), null, 2);
      }
    };

    const getPrivatizedAddress = (address) => {
      return `${address.substring(0, 5)}...${address.substring(
        address.length - 5,
        address.length
      )}`;
    };

    const buyToken = async () => {
      try {
        await tezosInterface.buy(token.value.price, token.value.id);
        // notifies user and resets values
        alerts.createAlert("Successfully purchased NFT!", "success");
      } catch (e) {
        alerts.createAlert("Something went wrong!", "error");
        throw new Error(e.toString());
      }
    };

    return {
      code,
      selected,
      highlightAll,
      fetchPreview,
      getPrivatizedAddress,
      buyToken,
      route,
      token,
    };
  },
});
</script>
