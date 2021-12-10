<template>
  <CodeBlock :code="code" class="mt-10" />
  <div class="flex items-center justify-end mt-3 text-gray-500">
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
  <div class="flex flex-col pt-12">
    <div class="flex items-center">
      <span class="text-4xl font-medium">{{ data.name }}</span>
    </div>
    <div class="flex items-center mt-1">
      <span class="text-xl text-gray-400"># {{ route.params.id }}</span>
    </div>
  </div>
</template>

<script>
import { defineComponent, onMounted, ref } from "vue";
import CodeBlock from "@/components/CodeBlock.vue";
import ToolTip from "@/components/Tooltip.vue";
import { useRoute } from "vue-router";
import { DownloadIcon, ClipboardCopyIcon } from "@heroicons/vue/outline";
import { highlightAll } from "prismjs";
import { useNftStore } from "@/stores/useNft";
import { storeToRefs } from "pinia";

export default defineComponent({
  components: {
    CodeBlock,
    ToolTip,
    DownloadIcon,
    ClipboardCopyIcon,
  },
  setup() {
    const route = useRoute();
    const isOpen = ref(false);
    const code = ref("");
    const data = ref({});
    const nftStore = useNftStore();
    const { nfts } = storeToRefs(nftStore);

    onMounted(async () => {
      const metadata = await fetch(nfts.value[route.params.id].metadataUri);
      data.value = await metadata.json();
      const asset = await fetch(data.value.assetUri);
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

    return { code, isOpen, copyToClipboard, highlightAll, route, data };
  },
});
</script>
