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
      <TabGroup>
        <TabList class="flex border-b space-x-10">
          <Tab
            v-for="title in ['Created', 'Activity']"
            as="template"
            :key="title"
            v-slot="{ selected }"
          >
            <button
              :class="[
                'py-4 text-black relative font-semibold transition duration-300 ease-in-out',
                selected ? '' : 'text-opacity-25 hover:text-opacity-100',
              ]"
            >
              <span
                class=""
                aria-hidden="true"
                :class="[
                  'block absolute w-full h-0.5 -bottom-0.5 left-0 transition duration-300 ease-in-out',
                  selected ? 'bg-cyan-500' : 'bg-transparent',
                ]"
              ></span>
              {{ title }}
            </button>
          </Tab>
        </TabList>

        <TabPanels class="mt-2">
          <TabPanel :class="['py-8 grid grid-cols-4 gap-6']">
            <DatasetCard
              v-for="(token, i) in tokens"
              :key="token.id"
              :dataset="token"
              :index="i"
            >
            </DatasetCard>
          </TabPanel>
          <TabPanel :class="['py-8']">
            <History :events="events" />
          </TabPanel>
        </TabPanels>
      </TabGroup>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import {
  getTokenMetadataByCreator,
  getEventsByCreator,
} from "@/services/graphql/queries";
import { ACCOUNT_IMAGE_PATH } from "@/constants";
import { useQuery, useResult } from "@vue/apollo-composable";
import DatasetCard from "@/components/Dataset/DatasetCard.vue";
import { TabGroup, TabList, TabPanel, Tab } from "@headlessui/vue";
import History from "@/components/History/History.vue";

export default defineComponent({
  components: {
    TabGroup,
    TabList,
    TabPanel,
    Tab,
    DatasetCard,
    History,
  },
  setup() {
    const route = useRoute();
    const creatorId = route.params.address;

    const { result: tokenResult } = useQuery(
      getTokenMetadataByCreator,
      () => ({
        creatorId,
        offset: 0,
        limit: 12,
      }),
      {
        fetchPolicy: "cache-and-network",
      }
    );

    const { result: eventResult } = useQuery(
      getEventsByCreator,
      () => ({
        creatorId,
      }),
      {
        fetchPolicy: "cache-and-network",
      }
    );

    const tokens = useResult(tokenResult, null, ({ token }) => token);
    const events = useResult(eventResult, null, ({ event }) => event);

    return {
      route,
      tokens,
      events,
      ACCOUNT_IMAGE_PATH,
    };
  },
});
</script>
