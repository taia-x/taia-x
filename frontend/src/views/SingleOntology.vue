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
      <ToolTip :isOpen="isOpen" :text="'Copied!'" @close="isOpen = false" />
    </button>
  </div>
  <div class="flex flex-col pt-12">
    <div class="flex items-center">
      <span class="text-4xl font-medium">Name of Ontology</span>
    </div>
    <div class="flex items-center mt-1">
      <span class="text-xl text-gray-400"># 733342</span>
    </div>
  </div>
</template>

<script>
import { defineComponent, onMounted, ref } from "vue";
import CodeBlock from "@/components/Utils/CodeBlock.vue";
import ToolTip from "@/components/Utils/Tooltip.vue";
import { useRoute, useRouter } from "vue-router";
import { DownloadIcon, ClipboardCopyIcon } from "@heroicons/vue/outline";
import { highlightAll } from "prismjs";

export default defineComponent({
  components: {
    CodeBlock,
    ToolTip,
    DownloadIcon,
    ClipboardCopyIcon,
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const isOpen = ref(false);
    const code = ref("");
    console.log(route.params.id);

    let data;
    onMounted(async () => {
      const result = await fetch("https://ipfs.io/ipfs/" + route.params.id);
      data = await result.json();
      console.log(data);
      code.value = JSON.stringify(data, null, 2);
    });

    const copyToClipboard = async () => {
      try {
        navigator.clipboard.writeText(code.value);
        isOpen.value = true;
        router.replace({ query: { fruit: "apple" } });
      } catch (e) {
        console.log(e);
      }
    };

    return { code, isOpen, copyToClipboard, highlightAll };
  },
});
</script>
