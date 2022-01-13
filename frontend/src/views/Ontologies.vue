<template>
  <div class="flex flex-col w-full pt-10 pb-24">
    <div class="flex items-center w-full space-x-4">
      <SearchBar
        @update:isOpen="$emit('update:isCreateOntologyModalOpen', $event)"
      />
    </div>
    <!-- <div class="flex items-center mt-4 space-x-4">
      <button class="flex items-center space-x-2 group">
        <SortAscendingIcon
          class="w-6 h-6 text-gray-400 transition duration-200 group-hover:text-gray-500"
        />
        <span
          class="text-gray-400 transition duration-200 group-hover:text-gray-900"
          >Name</span
        >
      </button>
      <button class="flex items-center space-x-2 group">
        <AdjustmentsIcon
          class="w-6 h-6 text-gray-400 transition duration-200 group-hover:text-gray-500"
        />
        <span
          class="text-gray-400 transition duration-200 group-hover:text-gray-900"
          >Filter</span
        >
      </button>
    </div> -->
    <div class="grid grid-cols-4 gap-6 mt-16">
      <router-link
        class="flex flex-col justify-between w-full p-4 transition duration-200 transform bg-gray-100 border-gray-300 rounded-lg  hover:scale-105 h-96 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        v-for="(ontology, index) in ontologies"
        :key="ontology.assetUri"
        :index="index"
        :to="
          '/ontologies/' +
          ontology.assetUri.substring(ontology.assetUri.indexOf('Qm'))
        "
        :ontology="ontology"
      >
      </router-link>
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
//import { AdjustmentsIcon, SortAscendingIcon } from "@heroicons/vue/outline";
import SearchBar from "@/components/SearchBar.vue";

export default defineComponent({
  components: {
    //AdjustmentsIcon,
    //SortAscendingIcon,
    SearchBar,
  },
});
</script>
