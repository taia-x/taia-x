<template>
  <div class="grid grid-cols-4 gap-6" v-if="tokens">
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
import { useRoute } from "vue-router";
import { getFilteredTokenMetadata } from "@/services/graphql/queries";
import { useQuery, useResult } from "@vue/apollo-composable";
import TokenCard from "@/components/TokenCard/TokenCard.vue";

export default defineComponent({
  components: {
    TokenCard,
  },
  setup() {
    const route = useRoute();
    const address = route.params.address;

    const query = getFilteredTokenMetadata(
      `{events: { recipient_id: { _eq: ${address}}}}`
    );

    const { result } = useQuery(query, null, {
      fetchPolicy: "cache-and-network",
    });
    const tokens = useResult(result, null, ({ token }) => token);

    return {
      route,
      tokens,
    };
  },
});
</script>
