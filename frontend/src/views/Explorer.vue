<template>
  <div class="flex flex-col w-full pt-10 pb-24">
    <div class="flex items-center w-full space-x-4">
      <SearchBar />
    </div>
    <div class="grid grid-cols-4 gap-6 mt-16" v-if="loading">
      <TokenCardSkeleton
        class="w-full h-56 transition duration-200 border-2 border-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500"
        v-for="i in 10"
        :key="i"
        :index="i"
      />
    </div>
    <div class="grid grid-cols-4 gap-6 mt-16" v-if="!loading">
      <span
        v-if="!tokens.length"
        class="absolute w-full text-sm font-semibold text-center text-gray-700"
        >No Datasets available!</span
      >
      <router-link
        class="w-full h-56 transition duration-200 transform border-2 border-gray-100 rounded-lg hover:shadow-xl hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        v-for="(token, index) in tokens"
        :key="token.id"
        :index="index"
        :to="'/explore/' + token.id"
      >
        <TokenCard :token="token" />
      </router-link>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SearchBar from "@/components/Explorer/SearchBar.vue";
import TokenCard from "@/components/TokenCard/TokenCard.vue";
import TokenCardSkeleton from "@/components/TokenCard/TokenCardSkeleton.vue";
import { useQuery, useResult } from "@vue/apollo-composable";
import { getTokenMetadata } from "@/services/graphql/queries";

export default defineComponent({
  components: {
    SearchBar,
    TokenCard,
    TokenCardSkeleton,
  },
  setup() {
    // fetches 12 tokens from contract when component mounts
    const { result, loading } = useQuery(
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
      loading,
    };
  },
});
</script>
