<template>
  <div class="container mx-auto space-y-8">
    <div class="flex items-center space-x-8">
      <div>
        <img
          :src="`${ACCOUNT_IMAGE_PATH}${address}`"
          class="h-32 w-32 rounded-full"
        />
      </div>
      <h1>{{ address }}</h1>
    </div>
    <div>
      <TabGroup>
        <TabList class="flex border-b space-x-10">
          <Tab
            v-for="title in Object.keys(tabs)"
            as="template"
            :key="title"
            v-slot="{ selected }"
          >
            <button
              :class="[
                'py-4 text-black relative font-semibold transition duration-300 ease-in-out capitalize',
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
          <TabPanel>
            <div :class="['py-8 grid grid-cols-4 gap-6']" v-if="tabs.collected">
              <router-link
                class="w-full h-56 transition duration-200 transform border-2 border-gray-100 rounded-lg hover:shadow-xl hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
                v-for="(token, index) in tabs.collected"
                :key="'collected-' + token.id"
                :index="index"
                :to="'/explore/' + token.id"
              >
                <TokenCard :token="token" />
              </router-link>
            </div>
          </TabPanel>

          <TabPanel>
            <div :class="['py-8 grid grid-cols-4 gap-6']" v-if="tabs.created">
              <router-link
                class="w-full h-56 transition duration-200 transform border-2 border-gray-100 rounded-lg hover:shadow-xl hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
                v-for="(token, index) in tabs.created"
                :key="'created-' + token.id"
                :index="index"
                :to="'/explore/' + token.id"
              >
                <TokenCard :token="token" />
              </router-link>
            </div>
          </TabPanel>

          <TabPanel>
            <div :class="['py-8 grid grid-cols-4 gap-6']" v-if="tabs.certified">
              <router-link
                class="w-full h-56 transition duration-200 transform border-2 border-gray-100 rounded-lg hover:shadow-xl hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
                v-for="(token, index) in tabs.certified"
                :key="'certified-' + token.id"
                :index="index"
                :to="'/explore/' + token.id"
              >
                <TokenCard :token="token" />
              </router-link>
            </div>
          </TabPanel>

          <TabPanel :class="['py-8']" v-if="tabs.activity">
            <History :events="tabs.activity" />
          </TabPanel>
        </TabPanels>
      </TabGroup>
    </div>
  </div>
</template>

<script>
import { defineComponent, reactive } from "vue";
import { useRoute } from "vue-router";
import {
  getTokenMetadataByCreator,
  getTokenMetadataByCollector,
  getUncertifiedTokenMetadata,
  getEventsByAccount,
} from "@/services/graphql/queries";
import { ACCOUNT_IMAGE_PATH } from "@/constants";
import { useQuery, useResult } from "@vue/apollo-composable";
import TokenCard from "@/components/TokenCard/TokenCard.vue";
import { TabGroup, TabList, Tab, TabPanels, TabPanel } from "@headlessui/vue";
import History from "@/components/History/History.vue";

export default defineComponent({
  components: {
    TabGroup,
    TabList,
    TabPanel,
    TabPanels,
    Tab,
    TokenCard,
    History,
  },
  setup() {
    const route = useRoute();
    const address = route.params.address;

    const tabs = reactive({
      collected: [],
      created: [],
      certified: [],
      activity: [],
    });

    const queryResult = (option, query, id) => {
      const { result } = useQuery(query, () => option, {
        fetchPolicy: "cache-and-network",
      });
      const value = useResult(result, null, (v) => v[id]);
      return value;
    };
    tabs.created = queryResult(
      {
        creatorId: address,
      },
      getTokenMetadataByCreator,
      "token"
    );

    tabs.collected = queryResult(
      {
        collectorId: address,
      },
      getTokenMetadataByCollector,
      "token"
    );

    tabs.certified = queryResult({}, getUncertifiedTokenMetadata, "token");

    tabs.activity = queryResult(
      {
        accountId: address,
      },
      getEventsByAccount,
      "event"
    );

    // const collected = queryResult(`{creator_id: { _eq: ${creatorId}}}`);
    // const created = queryResult(`{creator_id: { _eq: ${creatorId}}}`);
    // const certified = queryResult(`{ cert_state: {_eq: "pending"}}`);
    // const events = queryResult(
    //   `{_or: [{ caller_id: { _eq: ${creatorId} } }{ recipient_id: { _eq: ${creatorId} } }]}`,
    //   getFilteredEvents,
    //   "event"
    // );

    return {
      route,
      tabs,
      ACCOUNT_IMAGE_PATH,
      address,
    };
  },
});
</script>
