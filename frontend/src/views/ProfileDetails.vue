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
      <TabGroup manual :defaultIndex="2">
        <TabList class="flex border-b space-x-10">
          <Tab
            v-for="title in tabs"
            as="template"
            :key="title"
            v-slot="{ selected }"
          >
            <router-link
              :class="[
                'py-4 text-black relative font-semibold transition duration-300 ease-in-out capitalize',
                selected ? '' : 'text-opacity-25 hover:text-opacity-100',
              ]"
              :to="title.toLowerCase()"
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
            </router-link>
          </Tab>
        </TabList>
      </TabGroup>

      <div class="mt-2">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import { ACCOUNT_IMAGE_PATH } from "@/constants";
import { TabGroup, TabList, Tab } from "@headlessui/vue";

export default defineComponent({
  components: {
    TabGroup,
    TabList,
    Tab,
  },
  setup() {
    const route = useRoute();
    const address = route.params.address;

    const tabs = ["collected", "created", "certified", "activity"];

    return {
      route,
      tabs,
      ACCOUNT_IMAGE_PATH,
      address,
    };
  },
});
</script>
