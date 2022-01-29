<template>
  <div class="container mx-auto space-y-8">
    <div class="flex items-center space-x-8">
      <div>
        <img
          :src="`${ACCOUNT_IMAGE_PATH}${address}`"
          class="h-32 w-32 rounded-full"
        />
      </div>
      <h1>{{ route.params.address }}</h1>
    </div>
    <div>
      <RouterTabGroup>
        <RouterTab
          v-for="(tokens, idx) in Object.values(tabs)"
          :key="idx"
          :title="Object.keys(tabs)[idx]"
          :to="Object.keys(tabs)[idx].toLowerCase()"
          :class="['py-8 grid grid-cols-4 gap-6']"
        >
          <DatasetCard
            v-for="(token, i) in tokens"
            :key="idx + token.id"
            :dataset="token"
            :index="i"
          >
          </DatasetCard>
        </RouterTab>
      </RouterTabGroup>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useRoute } from "vue-router";
import { getTokenMetadataByCreator } from "@/services/graphql/queries";
import { ACCOUNT_IMAGE_PATH } from "@/constants";
import { useQuery, useResult } from "@vue/apollo-composable";
import DatasetCard from "@/components/Dataset/DatasetCard.vue";
import RouterTab from "@/components/Utils/RouterTab/RouterTab.vue";
import RouterTabGroup from "@/components/Utils/RouterTab/RouterTabGroup.vue";

export default defineComponent({
  components: {
    RouterTabGroup,
    RouterTab,
    DatasetCard,
  },
  setup() {
    const route = useRoute();

    const { result } = useQuery(
      getTokenMetadataByCreator,
      () => ({
        creatorId: route.params.address,
        offset: 0,
        limit: 12,
      }),
      {
        fetchPolicy: "cache-and-network",
      }
    );
    // stores result in tokens when result is loaded
    const tokens = useResult(result, null, ({ token }) => token);

    let tabs = ref({
      Collected: tokens,
      Created: tokens,
      Certified: tokens,
      Activity: tokens,
    });

    return {
      route,
      tabs,
      ACCOUNT_IMAGE_PATH,
    };
  },
});
</script>
