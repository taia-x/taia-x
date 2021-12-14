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
        <!-- Colors -->
        <!-- <div>
          <h3 class="text-sm font-medium text-gray-900">Color</h3>

          <RadioGroup v-model="selectedColor" class="mt-4">
            <RadioGroupLabel class="sr-only"> Choose a color </RadioGroupLabel>
            <div class="flex items-center space-x-3">
              <RadioGroupOption
                as="template"
                v-for="color in product.colors"
                :key="color.name"
                :value="color"
                v-slot="{ active, checked }"
              >
                <div
                  :class="[
                    color.selectedClass,
                    active && checked ? 'ring ring-offset-1' : '',
                    !active && checked ? 'ring-2' : '',
                    '-m-0.5 relative p-0.5 rounded-full flex items-center justify-center cursor-pointer focus:outline-none',
                  ]"
                >
                  <RadioGroupLabel as="p" class="sr-only">
                    {{ color.name }}
                  </RadioGroupLabel>
                  <span
                    aria-hidden="true"
                    :class="[
                      color.class,
                      'h-8 w-8 border border-black border-opacity-10 rounded-full',
                    ]"
                  />
                </div>
              </RadioGroupOption>
            </div>
          </RadioGroup>
        </div> -->

        <!-- Sizes -->
        <!-- <div class="mt-10">
          <div class="flex items-center justify-between">
            <h3 class="text-sm font-medium text-gray-900">Size</h3>
            <a
              href="#"
              class="text-sm font-medium text-indigo-600 hover:text-indigo-500"
              >Size guide</a
            >
          </div>

          <RadioGroup v-model="selectedSize" class="mt-4">
            <RadioGroupLabel class="sr-only"> Choose a size </RadioGroupLabel>
            <div class="grid grid-cols-4 gap-4 sm:grid-cols-8 lg:grid-cols-4">
              <RadioGroupOption
                as="template"
                v-for="size in product.sizes"
                :key="size.name"
                :value="size"
                :disabled="!size.inStock"
                v-slot="{ active, checked }"
              >
                <div
                  :class="[
                    size.inStock
                      ? 'bg-white shadow-sm text-gray-900 cursor-pointer'
                      : 'bg-gray-50 text-gray-200 cursor-not-allowed',
                    active ? 'ring-2 ring-indigo-500' : '',
                    'group relative border rounded-md py-3 px-4 flex items-center justify-center text-sm font-medium uppercase hover:bg-gray-50 focus:outline-none sm:flex-1 sm:py-6',
                  ]"
                >
                  <RadioGroupLabel as="p">
                    {{ size.name }}
                  </RadioGroupLabel>
                  <div
                    v-if="size.inStock"
                    :class="[
                      active ? 'border' : 'border-2',
                      checked ? 'border-indigo-500' : 'border-transparent',
                      'absolute -inset-px rounded-md pointer-events-none',
                    ]"
                    aria-hidden="true"
                  />
                  <div
                    v-else
                    aria-hidden="true"
                    class="absolute border-2 border-gray-200 rounded-md pointer-events-none -inset-px"
                  >
                    <svg
                      class="absolute inset-0 w-full h-full text-gray-200 stroke-2 "
                      viewBox="0 0 100 100"
                      preserveAspectRatio="none"
                      stroke="currentColor"
                    >
                      <line
                        x1="0"
                        y1="100"
                        x2="100"
                        y2="0"
                        vector-effect="non-scaling-stroke"
                      />
                    </svg>
                  </div>
                </div>
              </RadioGroupOption>
            </div>
          </RadioGroup>
        </div> -->

        <!-- <button
          type="submit"
          class="flex items-center justify-center w-full px-8 py-3 mt-10 text-base font-medium text-white bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Add to bag
        </button> -->
        <button
          v-wave
          class="flex items-center justify-center w-32 px-3 py-2 text-base text-white transition duration-300 ease-in-out transform rounded-md  h-11 bg-cyan-500 hover:bg-cyan-600 whitespace-nowrap focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
          @click.prevent="$emit('update:isOpen', true)"
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
