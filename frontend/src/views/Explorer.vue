<template>
  <div class="flex flex-col w-full pt-10 pb-24">
    <div class="flex items-center w-full space-x-4">
      <SearchBar
        @update:isOpen="isCreateDatasetModalOpen = true"
        @create:clicked="$router.push('/create')"
      />
    </div>
    <div class="grid grid-cols-4 gap-6 mt-16" v-if="tokens">
      <DatasetCard
        v-for="(token, index) in tokens"
        :key="token.id"
        :dataset="token"
        :index="index"
      >
      </DatasetCard>
    </div>
    <div
      class="flex items-center justify-between mt-16"
      v-if="tokens && tokens.length"
    >
      <div class="flex items-center space-x-2">
        <button
          v-for="i in [1]"
          :key="i"
          class="flex items-center w-10 h-10 p-3 rounded-md hover:bg-gray-100"
          :class="i === 1 ? 'text-white bg-cyan-500 hover:bg-cyan-600' : ''"
        >
          <span class="mx-auto font-medium">{{ i }}</span>
        </button>
      </div>
      <div class="flex items-center space-x-6">
        <button class="font-medium text-gray-500">Previous</button>
        <button class="font-medium hover:text-cyan-500">Next</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import SearchBar from "@/components/Explorer/SearchBar.vue";
import DatasetCard from "@/components/Dataset/DatasetCard.vue";

import { useQuery, useResult } from "@vue/apollo-composable";
import { getTokenMetadata } from "@/services/graphql/queries";

export default defineComponent({
  components: {
    SearchBar,
    DatasetCard,
  },
  setup() {
    const isCreateDatasetModalOpen = ref(false);
    // fetches 12 tokens from contract when component mounts
    const { result } = useQuery(
      getTokenMetadata,
      () => ({
        offset: 0,
        limit: 12,
      }),
      {
        fetchPolicy: "cache-and-network",
      }
    );
    // stores result in tokens when result is loaded
    const tokens = useResult(result, null, ({ token }) => token);

    return { tokens, isCreateDatasetModalOpen };
  },
});
</script>
