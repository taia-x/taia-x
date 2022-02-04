<template>
  <ProfileDetailsTab :tokens="tokens" :loading="loading"
    >No available Datasets!</ProfileDetailsTab
  >
</template>

<script>
import { defineComponent, watch } from "vue";
import { useRoute } from "vue-router";
import { getFilteredTokenMetadata } from "@/services/graphql/queries";
import { useQuery, useResult } from "@vue/apollo-composable";
import ProfileDetailsTab from "@/components/ProfileDetailsTabs/ProfileDetailsTab.vue";

export default defineComponent({
  components: {
    ProfileDetailsTab,
  },
  setup() {
    const route = useRoute();

    const query = getFilteredTokenMetadata(
      `{ cert_state: { _eq: "pending" } }`
    );

    const { result, loading, refetch } = useQuery(query, null, {
      fetchPolicy: "cache-and-network",
    });

    const tokens = useResult(result, null, ({ token }) => token);

    watch(route, () => {
      if (route.name === "certified") refetch();
    });

    return {
      tokens,
      loading,
    };
  },
});
</script>
