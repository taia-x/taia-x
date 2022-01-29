<template>
  <TabGroup as="div" :selectedIndex="selectedIndex">
    <TabList class="flex border-b space-x-10">
      <Tab
        v-for="tab in tabs"
        as="template"
        :key="tab.to"
        v-slot="{ selected }"
      >
        <router-link
          :to="tab.to"
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
          {{ tab.title }} {{ selectedIndex }}
        </router-link>
      </Tab>
    </TabList>

    <TabPanels class="mt-2">
      <slot></slot>
    </TabPanels>
  </TabGroup>
</template>

<script>
import { defineComponent, computed } from "vue";
import { TabGroup, TabList, Tab, TabPanels } from "@headlessui/vue";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

export default defineComponent({
  components: {
    TabGroup,
    TabList,
    Tab,
    TabPanels,
  },
  setup(props, { slots }) {
    const route = useRoute();
    const tabs = ref([]);

    onMounted(function () {
      tabs.value = slots.default()[0].children.map((c) => {
        return { title: c.props.title, to: c.props.to };
      });
    });

    const selectedIndex = computed(() =>
      tabs.value.findIndex((t) => t.to === route.params.tab)
    );

    return { tabs, selectedIndex };
  },
});
</script>
