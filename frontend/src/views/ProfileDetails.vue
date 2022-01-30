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
            v-for="title in ['Collected', 'Created', 'Certified', 'Activity']"
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
          <TabPanel>
            <div :class="['py-8 grid grid-cols-4 gap-6']" v-if="tokens">
              <router-link
                class="w-full h-56 transition duration-200 transform border-2 border-gray-100 rounded-lg hover:shadow-xl hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
                v-for="(token, index) in tokens"
                :key="'collected-' + token.id"
                :index="index"
                :to="'/explore/' + token.id"
              >
                <TokenCard :token="token" />
              </router-link>
            </div>
          </TabPanel>

          <TabPanel>
            <div :class="['py-8 grid grid-cols-4 gap-6']" v-if="tokens">
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
          </TabPanel>

          <TabPanel>
            <div :class="['py-8 grid grid-cols-4 gap-6']" v-if="tokens">
              <router-link
                class="w-full h-56 transition duration-200 transform border-2 border-gray-100 rounded-lg hover:shadow-xl hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
                v-for="(token, index) in tokens"
                :key="'certified-' + token.id"
                :index="index"
                :to="'/explore/' + token.id"
              >
                <TokenCard :token="token" />
              </router-link>
            </div>
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
import { getSingleCreator } from "@/services/graphql/queries";
import { ACCOUNT_IMAGE_PATH } from "@/constants";
import { useQuery, useResult } from "@vue/apollo-composable";
import TokenCard from "@/components/TokenCard/TokenCard.vue";
import { TabGroup, TabList, TabPanel, Tab } from "@headlessui/vue";
import History from "@/components/History/History.vue";

export default defineComponent({
  components: {
    TabGroup,
    TabList,
    TabPanel,
    Tab,
    TokenCard,
    History,
  },
  setup() {
    const route = useRoute();
    const creatorId = route.params.address;

    const { result } = useQuery(
      getSingleCreator,
      () => ({
        creatorId,
      }),
      {
        fetchPolicy: "cache-and-network",
      }
    );

    const tokens = useResult(result, null, ({ token }) => token);
    const events = useResult(result, null, ({ event }) => event);

    return {
      route,
      tokens,
      events,
      ACCOUNT_IMAGE_PATH,
    };
  },
});
</script>
