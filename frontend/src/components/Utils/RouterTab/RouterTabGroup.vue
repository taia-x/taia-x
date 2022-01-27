<template>
  <div  >
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
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { TabGroup, TabList, Tab, TabPanels, TabPanel } from "@headlessui/vue";

export default defineComponent({
  components: {
    TabGroup,
    TabList,
    Tab,
    TabPanels,
    TabPanel,
  },
  setup() {
  },
});
</script>
