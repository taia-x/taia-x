<template>
  <Terminal
    :code="code"
    :file="selected"
    class="mt-10 filter drop-shadow-2xl"
  />
  <!-- <div class="flex items-center justify-end mt-4 text-gray-500">
    <button
      class="z-10 flex items-center space-x-1 hover:text-gray-900"
      @click.prevent="highlightAll()"
    >
      <span>Download</span>
      <DownloadIcon class="w-5 h-5" />
    </button>
    <button
      class="relative z-10 flex items-center space-x-1 hover:text-gray-900"
      @click.prevent="copyToClipboard()"
    >
      <span class="pl-4">Copy</span>
      <ClipboardCopyIcon class="w-5 h-5" />
      <ToolTip :isOpen="isOpen" :text="'Copied!'" @closed="isOpen = false" />
    </button>
  </div> -->
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
    class="flex items-center px-3 text-white transition duration-300 ease-in-out transform border-2 border-b-4 rounded-md h-10 bg-cyan-500 hover:bg-cyan-600 text-md whitespace-nowrap border-cyan-700 hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
  >
    Buy for 5 ꜩ
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
          <Tooltip class="group" @click.prevent="fetchOntology(file)">
            <template #element
              ><EyeIcon
                class="w-5 h-5 text-gray-400 transition-colors duration-150 hover:text-gray-700"
            /></template>
            <template #text>Show Ontology</template>
          </Tooltip>
        </div>
      </div>
    </div>
    <div class="space-y-4">
      <h3
        class="flex items-center space-x-1 text-xl font-semibold text-gray-900"
      >
        <span>History</span>
        <InformationCircleIcon
          class="w-5 h-5 text-gray-400 transform -translate-y-1"
        />
      </h3>
      <div v-if="token && token.events">
        <div
          class="grid grid-cols-5 grid-rows-1 px-3 py-2 font-medium text-gray-900 border-t-2 border-l-2 border-r-2 border-gray-100 rounded-t-lg"
        >
          <div>Event</div>
          <div>From</div>
          <div>To</div>
          <div>Price</div>
          <div>Date</div>
        </div>
        <div
          class="grid grid-cols-5 grid-rows-1 px-3 py-2 text-base text-gray-700 border-2 border-gray-100"
          :class="index + 1 === token.events.length ? 'rounded-b-lg' : ''"
          v-for="(event, index) in token.events"
          :key="event.id"
          :index="index"
        >
          <div class="flex items-center space-x-2">
            <DocumentAddIcon
              v-if="event.event_type === 'mint'"
              class="w-5 h-5 text-gray-700"
            />
            <BadgeCheckIcon
              v-if="event.event_type === 'certify'"
              class="w-5 h-5 text-gray-700"
            />
            <ShoppingBagIcon
              v-if="event.event_type === 'purchase'"
              class="w-5 h-5 text-gray-700"
            />
            <BanIcon
              v-if="event.event_type === 'reject'"
              class="w-5 h-5 text-gray-700"
            />
            <span class="truncate">
              {{
                event.event_type[0].toUpperCase() + event.event_type.slice(1)
              }}
            </span>
          </div>
          <div v-if="event" class="flex">
            <a
              :href="`https://tzkt.io/${event.creator_id}`"
              target="_blank"
              class="flex items-center space-x-2"
            >
              <img
                v-if="event.creator_id"
                :src="`https://services.tzkt.io/v1/avatars/${event.creator_id}`"
                class="w-10 h-10 my-auto"
              />
              <span class="truncate">{{
                event.creator_id ? getPrivatizedAddress(event.creator_id) : "-"
              }}</span>
            </a>
          </div>
          <div v-if="event" class="flex">
            <a
              target="_blank"
              :href="`https://tzkt.io/${event.recipient_id}`"
              class="flex items-center space-x-2"
            >
              <img
                v-if="event.recipient_id"
                :src="`https://services.tzkt.io/v1/avatars/${event.recipient_id}`"
                class="w-10 h-10 my-auto"
              />
              <span class="truncate">{{
                event.recipient_id
                  ? getPrivatizedAddress(event.recipient_id)
                  : "-"
              }}</span>
            </a>
          </div>
          <div class="flex items-center">
            <span class="truncate">{{ event.price || "-" }}</span>
          </div>
          <div class="flex items-center">
            <a
              class="truncate"
              target="_blank"
              :href="`https://tzkt.io/${event.ophash}`"
              >{{ new Date(event.timestamp).toDateString() }}</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, watchEffect, ref } from "vue";
import Terminal from "@/components/Utils/Terminal.vue";
import { useRoute } from "vue-router";
import {
  ClockIcon,
  DocumentIcon,
  DocumentAddIcon,
  InformationCircleIcon,
  DocumentTextIcon,
  ShoppingBagIcon,
  BadgeCheckIcon,
  BanIcon,
  EyeIcon,
} from "@heroicons/vue/outline";
import { highlightAll } from "prismjs";
import { ipfsInterface } from "@/services";
import { useQuery, useResult } from "@vue/apollo-composable";
import { getSingleTokenMetadata } from "@/services/graphql/queries";
import Tooltip from "@/components/Utils/Tooltip.vue";

export default defineComponent({
  components: {
    Terminal,
    ClockIcon,
    DocumentIcon,
    InformationCircleIcon,
    ShoppingBagIcon,
    BanIcon,
    DocumentAddIcon,
    DocumentTextIcon,
    BadgeCheckIcon,
    EyeIcon,
    Tooltip,
  },
  setup() {
    const route = useRoute();
    //const isOpen = ref(false);
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
        const asset = await fetch(
          ipfsInterface.makeGatewayURL(
            token_metadata.value.files[0].ontologyUri
          )
        );
        code.value = JSON.stringify(await asset.json(), null, 2);
      }
    });

    const fetchOntology = async (file) => {
      if (file.ontologyUri && selected.value.fileName !== file.fileName) {
        selected.value = file;
        const asset = await fetch(
          ipfsInterface.makeGatewayURL(file.ontologyUri)
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

    // copies content of artifact json to clipboard
    // const copyToClipboard = async () => {
    //   try {
    //     navigator.clipboard.writeText(code.value);
    //     isOpen.value = true;
    //   } catch (e) {
    //     console.log(e);
    //   }
    // };

    return {
      code,
      //isOpen,
      selected,
      //copyToClipboard,
      highlightAll,
      fetchOntology,
      getPrivatizedAddress,
      route,
      token,
    };
  },
});
</script>
