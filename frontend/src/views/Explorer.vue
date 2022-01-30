<template>
  <div class="flex flex-col w-full pt-10 pb-24">
    <div class="flex items-center w-full space-x-4">
      <SearchBar />
    </div>
    <div class="grid grid-cols-4 gap-6 mt-16" v-if="tokens">
      <router-link
        class="w-full h-56 transition duration-200 transform border-2 border-gray-100 rounded-lg hover:shadow-xl hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        v-for="(token, index) in tokens"
        :key="token.id"
        :dataset="token"
        :index="index"
      >
        <TokenCard :token="token" />
      </router-link>
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
import { defineComponent } from "vue";
import SearchBar from "@/components/Explorer/SearchBar.vue";
import TokenCard from "@/components/TokenCard/TokenCard.vue";
import { useQuery, useResult } from "@vue/apollo-composable";
import { getTokenMetadata } from "@/services/graphql/queries";

export default defineComponent({
  components: {
    SearchBar,
    TokenCard,
  },
  setup() {
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

    return {
      tokens,
    };
  },
});
</script>
