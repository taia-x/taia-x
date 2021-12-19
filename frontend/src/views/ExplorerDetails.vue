<template>
  <Terminal :code="code" class="mt-10" />
  <div class="flex items-center justify-end mt-4 text-gray-500">
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
  </div>
  <div
    class="
      max-w-2xl
      mx-auto
      pt-10
      pb-16
      lg:max-w-7xl
      lg:pt-16
      lg:pb-24
      lg:grid
      lg:grid-cols-3
      lg:grid-rows-[auto,auto,1fr]
      lg:gap-x-8
    "
  >
    <div class="lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8">
      <h1
        class="text-2xl font-extrabold tracking-tight text-gray-900 sm:text-3xl"
      >
        {{ data.name }}
      </h1>
      <span class="mt-1 text-xl text-gray-400"># {{ route.params.id }}</span>
    </div>

    <!-- Options -->
    <div class="mt-4 lg:mt-0 lg:row-span-3">
      <h2 class="sr-only">NFT description</h2>
      <p class="flex items-center text-3xl text-gray-900">
        <span class="transform -translate-y-1">ꜩ</span>
        <span>&nbsp;3.256</span>
      </p>

      <!-- Reviews -->
      <div class="mt-6">
        <h3 class="sr-only">Reviews</h3>
        <div class="flex items-center">
          <div class="flex items-center">
            <StarIcon
              v-for="rating in [0, 1, 2, 3, 4]"
              :key="rating"
              :class="[
                4 > rating ? 'text-gray-900' : 'text-gray-200',
                'h-5 w-5 flex-shrink-0',
              ]"
              aria-hidden="true"
            />
          </div>
          <p class="sr-only">4 out of 5 stars</p>
          <a
            href="#"
            class="ml-3 text-sm font-medium text-cyan-500 hover:text-cyan-600"
            >117 reviews</a
          >
        </div>
      </div>

      <form class="mt-10">
        <button
          v-wave
          class="flex items-center justify-center w-32 px-3 py-2 text-base text-white transition duration-300 ease-in-out transform rounded-md  h-11 bg-cyan-500 hover:bg-cyan-600 whitespace-nowrap focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
        >
          <ShoppingBagIcon class="w-5 h-5 transform -translate-x-1" />
          <span>Buy</span>
        </button>
      </form>
    </div>

    <div
      class="py-10  lg:pt-6 lg:pb-16 lg:col-start-1 lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8"
    >
      <!-- Description and details -->
      <div>
        <h3 class="sr-only">Description</h3>
        <div class="space-y-6">
          <p class="text-base text-gray-900">{{ data.description }}</p>
        </div>
      </div>

      <div class="mt-10">
        <h3 class="text-sm font-medium text-gray-900">Highlights</h3>
        <div class="mt-4">
          <ul role="list" class="pl-4 space-y-2 text-sm list-disc">
            <li
              v-for="highlight in [0, 1, 2]"
              :key="highlight"
              class="text-gray-400"
            >
              <span class="text-gray-600">...</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="mt-10">
        <h2 class="text-sm font-medium text-gray-900">Details</h2>
        <div class="mt-4 space-y-6">
          <p class="text-sm text-gray-600">...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, onMounted, ref } from "vue";
import Terminal from "@/components/Utils/Terminal.vue";
import ToolTip from "@/components/Utils/Tooltip.vue";
import { useRoute } from "vue-router";
import {
  DownloadIcon,
  ClipboardCopyIcon,
  ShoppingBagIcon,
} from "@heroicons/vue/outline";
import { highlightAll } from "prismjs";
import { useNftStore } from "@/stores/useNft";
import { storeToRefs } from "pinia";
import { ipfsInterface } from "@/services";
import { StarIcon } from "@heroicons/vue/solid";

export default defineComponent({
  components: {
    Terminal,
    ToolTip,
    ShoppingBagIcon,
    DownloadIcon,
    ClipboardCopyIcon,
    StarIcon,
  },
  setup() {
    const route = useRoute();
    const isOpen = ref(false);
    const code = ref("");
    const data = ref({});
    const nftStore = useNftStore();
    const { nfts } = storeToRefs(nftStore);

    // fetches metadata for nft from ipfs based on route parameter
    onMounted(async () => {
      const metadata = await fetch(
        ipfsInterface.makeGatewayURL(nfts.value[route.params.id].metadataUri)
      );
      data.value = await metadata.json();
      const asset = await fetch(
        ipfsInterface.makeGatewayURL(data.value.assetUri)
      );
      code.value = JSON.stringify(await asset.json(), null, 2);
    });

    // copies content of artifact json to clipboard
    const copyToClipboard = async () => {
      try {
        navigator.clipboard.writeText(code.value);
        isOpen.value = true;
      } catch (e) {
        console.log(e);
      }
    };

    return {
      code,
      isOpen,
      copyToClipboard,
      highlightAll,
      route,
      data,
    };
  },
});
</script>
