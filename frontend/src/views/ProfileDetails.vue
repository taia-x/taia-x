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
    <div v-if="tokens">
      <TabGroup>
        <TabList class="flex border-b space-x-10">
          <Tab
            v-for="category in Object.keys(categories)"
            as="template"
            :key="category"
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
              {{ category }}
            </button>
          </Tab>
        </TabList>

        <TabPanels class="mt-2">
          <TabPanel
            v-for="(posts, idx) in Object.values(categories)"
            :key="idx"
            :class="['py-8 grid grid-cols-4 gap-6']"
          >
            <DatasetCard
              v-for="(token, i) in tokens"
              :key="token.id"
              :dataset="token"
              :index="i"
            >
            </DatasetCard>
          </TabPanel>
        </TabPanels>
      </TabGroup>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useRoute } from "vue-router";
import { TabGroup, TabList, Tab, TabPanels, TabPanel } from "@headlessui/vue";
import { getTokenMetadata } from "@/services/graphql/queries";
import { ACCOUNT_IMAGE_PATH } from "@/constants";
import { useQuery, useResult } from "@vue/apollo-composable";
import DatasetCard from "@/components/Utils/Dataset/DatasetCard.vue";

export default defineComponent({
  components: {
    TabGroup,
    TabList,
    Tab,
    TabPanels,
    TabPanel,
    DatasetCard,
  },
  setup() {
    const route = useRoute();

    const { result } = useQuery(
      getTokenMetadata,
      () => ({
        offset: 0,
        limit: 12,
      }),
      {
        fetchPolicy: "cache-and-network",
      }
    );
    // stores result in tokens when result is loaded
    const tokens = useResult(result, null, ({ token }) => token);

    let categories = ref({
      Collected: [
        {
          id: 1,
          title: "Does drinking coffee make you smarter?",
          date: "5h ago",
          commentCount: 5,
          shareCount: 2,
        },
        {
          id: 2,
          title: "So you've bought coffee... now what?",
          date: "2h ago",
          commentCount: 3,
          shareCount: 2,
        },
      ],
      Created: [
        {
          id: 1,
          title: "Is tech making coffee better or worse?",
          date: "Jan 7",
          commentCount: 29,
          shareCount: 16,
        },
        {
          id: 2,
          title: "The most innovative things happening in coffee",
          date: "Mar 19",
          commentCount: 24,
          shareCount: 12,
        },
      ],
      Certified: [
        {
          id: 1,
          title: "Ask Me Anything: 10 answers to your questions about coffee",
          date: "2d ago",
          commentCount: 9,
          shareCount: 5,
        },
        {
          id: 2,
          title: "The worst advice we've ever heard about coffee",
          date: "4d ago",
          commentCount: 1,
          shareCount: 2,
        },
      ],
      Activity: [
        {
          id: 1,
          title: "Ask Me Anything: 10 answers to your questions about coffee",
          date: "2d ago",
          commentCount: 9,
          shareCount: 5,
        },
        {
          id: 2,
          title: "The worst advice we've ever heard about coffee",
          date: "4d ago",
          commentCount: 1,
          shareCount: 2,
        },
      ],
    });

    return {
      route,
      categories,
      tokens,
      ACCOUNT_IMAGE_PATH,
    };
  },
});
</script>
