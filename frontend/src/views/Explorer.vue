<template>
  <div class="flex flex-col w-full pt-10 pb-24">
    <div class="flex items-center w-full space-x-4">
      <div class="relative w-full group">
        <span class="absolute inset-y-0 left-0 flex items-center pl-4 group">
          <SearchIcon class="w-5 h-5 text-gray-500" />
        </span>
        <input
          type="text"
          name="first-name"
          id="first-name"
          autocomplete="given-name"
          placeholder="Search"
          class="block w-full pl-12 transition duration-300 border-2 border-gray-300 rounded-md  h-11 focus:ring-cyan-500 focus:border-cyan-500"
        />
      </div>
      <button
        v-wave
        class="
          flex
          items-center
          justify-center
          px-3
          py-2
          text-white
          transition
          duration-300
          ease-in-out
          transform
          border-2 border-b-4
          rounded-md
          h-11
          bg-cyan-500
          hover:bg-cyan-600
          text-md
          whitespace-nowrap
          border-cyan-700
          hover:-translate-y-0.5
          focus:outline-none
          focus:ring-2
          focus:ring-offset-2
          focus:ring-cyan-500
        "
        @click.prevent="$emit('update:isCreateDatasetModalOpen', true)"
      >
        <PlusIcon class="w-5 h-5 transform -translate-x-1" />
        <span>Create</span>
      </button>
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
    <div class="grid grid-cols-4 gap-4 mt-16">
      <button
        class="w-full transition duration-200 transform bg-gray-100 border-gray-300 rounded-lg  hover:scale-105 h-96 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        v-for="i in [1, 2, 3, 4]"
        :key="i"
        :index="i"
      ></button>
      <button
        class="w-full transition duration-200 transform bg-gray-100 border-gray-300 rounded-lg  hover:scale-105 h-96 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        style="animation-delay: 150ms; animation-fill-mode: backwards"
        v-for="i in [1, 2, 3, 4]"
        :key="i"
        :index="i"
      ></button>
      <button
        class="w-full transition duration-200 transform bg-gray-100 border-gray-300 rounded-lg  hover:scale-105 h-96 focus:outline-none focus:ring-2 focus:ring-cyan-500"
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
import { SearchIcon, PlusIcon } from "@heroicons/vue/solid";
import { AdjustmentsIcon, SortAscendingIcon } from "@heroicons/vue/outline";

export default defineComponent({
  components: {
    SearchIcon,
    PlusIcon,
    AdjustmentsIcon,
    SortAscendingIcon,
  },
});
</script>
