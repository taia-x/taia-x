<template>
  <div class="grid grid-cols-4 gap-6" v-if="loading">
    <TokenCardSkeleton
      class="w-full h-56 transition duration-200 border-2 border-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500"
      v-for="i in 10"
      :key="i"
      :index="i"
    />
  </div>
  <div class="grid grid-cols-4 gap-6" v-if="!loading">
    <span
      v-if="!tokens.length"
      class="absolute w-full text-sm font-semibold text-center text-gray-700"
      >No available Datasets!</span
    >
    <router-link
      class="w-full h-56 transition duration-200 transform border-2 border-gray-100 rounded-lg hover:shadow-xl hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
      v-for="(token, index) in tokens"
      :key="'created-' + token.id"
      :index="index"
      :to="'/explore/' + token.id"
    >
      <TokenCard :token="token" />
    </router-link>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { getFilteredTokenMetadata } from "@/services/graphql/queries";
import { useQuery, useResult } from "@vue/apollo-composable";
import TokenCard from "@/components/TokenCard/TokenCard.vue";
import TokenCardSkeleton from "@/components/TokenCard/TokenCardSkeleton.vue";

export default defineComponent({
  components: {
    TokenCard,
    TokenCardSkeleton,
  },
  setup() {
    const query = getFilteredTokenMetadata(
      `{ cert_state: { _eq: "pending" } }`
    );

    const { result } = useQuery(query, null, {
      fetchPolicy: "cache-and-network",
    });
    const tokens = useResult(result, null, ({ token }) => token);

    return {
      tokens,
    };
  },
});
</script>
