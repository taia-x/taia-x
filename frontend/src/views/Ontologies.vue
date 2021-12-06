<template>
  <div class="flex flex-col w-full pt-10 pb-24">
    <div class="flex items-center w-full space-x-4">
      <SearchBar
        @update:isOpen="$emit('update:isCreateOntologyModalOpen', $event)"
      />
    </div>
    <div class="flex items-center mt-4 space-x-4">
      <button class="flex items-center space-x-2 group">
        <SortAscendingIcon
          class="w-6 h-6 text-gray-400 transition duration-200  group-hover:text-gray-500"
        />
        <span
          class="text-gray-400 transition duration-200  group-hover:text-gray-900"
          >Name</span
        >
      </button>
      <button class="flex items-center space-x-2 group">
        <AdjustmentsIcon
          class="w-6 h-6 text-gray-400 transition duration-200  group-hover:text-gray-500"
        />
        <span
          class="text-gray-400 transition duration-200  group-hover:text-gray-900"
          >Filter</span
        >
      </button>
    </div>
    <div class="grid grid-cols-4 gap-6 mt-16">
      <router-link
        class="flex flex-col justify-between w-full p-4 transition duration-200 transform bg-gray-100 border-gray-300 rounded-lg  hover:scale-105 h-96 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        v-for="i in [1, 2, 3, 4]"
        :key="i"
        :index="i"
        :to="'/ontologies/' + i"
      >
        <div class="w-full h-32 bg-gray-200 rounded-lg"></div>
        <div
          class="flex items-center justify-between text-sm font-medium text-gray-400 "
        >
          <span>33 ꜩ</span>
          <span class="flex items-center space-x-1">
            <HeartIcon class="w-5 h-5" />
            <span>98</span>
          </span>
        </div>
      </router-link>
      <button
        class="w-full transition duration-200 transform bg-gray-100 rounded-lg  hover:scale-105 h-96 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        style="animation-delay: 150ms; animation-fill-mode: backwards"
        v-for="i in [1, 2, 3, 4]"
        :key="i"
        :index="i"
      ></button>
      <button
        class="w-full overflow-hidden transition duration-200 transform bg-gray-100 rounded-lg  hover:scale-105 h-96 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        style="animation-delay: 300ms; animation-fill-mode: backwards"
        v-for="i in [1, 2, 3, 4]"
        :key="i"
        :index="i"
      ></button>
    </div>
    <div class="flex items-center justify-between mt-16">
      <div class="flex items-center space-x-2">
        <button
          v-for="i in [0, 1, 2, 3]"
          :key="i"
          class="flex items-center w-10 h-10 p-3 rounded-md hover:bg-gray-100"
          :class="i === 0 ? 'text-white bg-cyan-500' : ''"
        >
          <span class="mx-auto font-medium">{{ i }}</span>
        </button>
        <div class="flex items-center w-10 h-10 p-3 rounded-md">
          <span class="font-medium">...</span>
        </div>
        <button
          v-for="i in [7, 8, 9]"
          :key="i"
          class="flex items-center w-10 h-10 p-3 rounded-md hover:bg-gray-100"
          :class="i === 0 ? 'text-white bg-cyan-500' : ''"
        >
          <span class="mx-auto font-medium">{{ i }}</span>
        </button>
      </div>
      <div class="flex items-center space-x-6">
        <button class="font-medium text-gray-500">Previous</button>
        <button class="font-medium hover:text-cyan-500">Next</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
  AdjustmentsIcon,
  SortAscendingIcon,
  HeartIcon,
} from "@heroicons/vue/outline";
import SearchBar from "@/components/SearchBar.vue";

export default defineComponent({
  components: {
    AdjustmentsIcon,
    SortAscendingIcon,
    SearchBar,
    HeartIcon,
  },
  setup() {
    const data = JSON.parse(`
    {
      "@id": "dtmi:taiax:battery;1",
      "@type": "Interface",
      "@context": "dtmi:dtdl:context;2",
      "contents": [
        {
          "@type": "Telemetry",
          "name": "battery_state",
          "schema": {
            "@type": "Object",
            "fields": [
              {
                "name": "state_of_charge",
                "schema": "float"
              },
              {
                "name": "u_out_inst",
                "schema": "float"
              },
              {
                "name": "i_out_inst",
                "schema": "float"
              },
              {
                "name": "temp_max",
                "schema": "float"
              },
              {
                "name": "temp_min",
                "schema": "float"
              }
            ]
          }
        }
      ]
    }`);

    const code = JSON.stringify(data, null, 2);

    return { code };
  },
});
</script>
