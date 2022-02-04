<template>
  <ProfileDetailsTab :tokens="tokens" :loading="loading"
    >No created Datasets!</ProfileDetailsTab
  >
</template>

<script>
import { defineComponent, watch } from "vue";
import { useRoute } from "vue-router";
import { getCreations } from "@/services/graphql/queries";
import { useQuery, useResult } from "@vue/apollo-composable";
import ProfileDetailsTab from "@/components/ProfileDetailsTabs/ProfileDetailsTab.vue";

export default defineComponent({
  components: {
    ProfileDetailsTab,
  },
  setup() {
    const route = useRoute();

    const { result, loading, refetch } = useQuery(
      getCreations,
      () => ({
        address: route.params.address,
      }),
      {
        fetchPolicy: "cache-and-network",
      }
    );

    const tokens = useResult(
      result,
      null,
      ({ account_by_pk }) => account_by_pk.creations
    );

    watch(route, () => {
      if (route.name === "created") refetch();
    });

    return {
      route,
      tokens,
      loading,
    };
  },
});
</script>
