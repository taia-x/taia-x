<template>
  <div class="container mx-auto space-y-8">
    <div class="flex items-center space-x-8">
      <div>
        <UserCircleIcon class="h-32 w-32 text-cyan-500 rounded-full" />
      </div>
      <h1>{{ route.params.address }}</h1>
    </div>
    <div>
      <TabGroup>
        <TabList class="flex border-b">
          <Tab
            v-for="category in Object.keys(categories)"
            as="template"
            :key="category"
            v-slot="{ selected }"
          >
            <button
              :class="[
                'px-6 py-3 text-black relative text-sm font-medium transition duration-300 ease-in-out',
                selected ? '' : 'text-opacity-25 hover:text-opacity-100',
              ]"
            >
              <span
                class=""
                aria-hidden="true"
                :class="[
                  'block absolute w-full h-px -bottom-px left-0 transition duration-300 ease-in-out',
                  selected ? 'bg-black' : 'bg-transparent',
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
            :class="['py-8']"
          >
            <ul>
              <li
                v-for="post in posts"
                :key="post.id"
                class="relative p-3 rounded-md hover:bg-coolGray-100"
              >
                <h3 class="text-sm font-medium leading-5">
                  {{ post.title }}
                </h3>

                <ul
                  class="flex mt-1 space-x-1 text-xs font-normal leading-4 text-coolGray-500"
                >
                  <li>{{ post.date }}</li>
                  <li>&middot;</li>
                  <li>{{ post.commentCount }} comments</li>
                  <li>&middot;</li>
                  <li>{{ post.shareCount }} shares</li>
                </ul>

                <a href="#" :class="['absolute inset-0 rounded-md']" />
              </li>
            </ul>
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
import { UserCircleIcon } from "@heroicons/vue/solid";

export default defineComponent({
  components: {
    TabGroup,
    TabList,
    Tab,
    TabPanels,
    TabPanel,
    UserCircleIcon,
  },
  setup() {
    const route = useRoute();
    let categories = ref({
      Recent: [
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
      Popular: [
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
      Trending: [
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
    };
  },
});
</script>
