<template>
  <ProfileDetailsTab :tokens="tokens" :loading="loading"
    >No collected Datasets!</ProfileDetailsTab
  >
</template>

<script>
import { defineComponent, watch } from "vue";
import { useRoute } from "vue-router";
import { getPurchases } from "@/services/graphql/queries";
import { useQuery, useResult } from "@vue/apollo-composable";
import ProfileDetailsTab from "@/components/ProfileDetailsTabs/ProfileDetailsTab.vue";

export default defineComponent({
  components: {
    ProfileDetailsTab,
  },
  setup() {
    const route = useRoute();

    const { result, loading, refetch } = useQuery(
      getPurchases,
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
      ({ account_by_pk }) => account_by_pk.purchases
    );

    watch(route, () => {
      if (route.name === "collected") refetch();
    });

    return {
      route,
      tokens,
      loading,
    };
  },
});
</script>
