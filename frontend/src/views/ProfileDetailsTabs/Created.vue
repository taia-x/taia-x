<template>
  <div class="grid grid-cols-4 gap-6" v-if="tokens">
      <TokenCard :token="token" />
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
