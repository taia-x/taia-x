<template>
  <div class="flex flex-col w-full pt-10 pb-24">
    <div class="flex items-center w-full space-x-4">
      <SearchBar
        @update:isOpen="isCreateDatasetModalOpen = true"
        @create:clicked="$router.push('/create')"
      />
    </div>
    <!-- <div class="flex items-center mt-4 space-x-4">
      <button class="flex items-center space-x-2 group" @click.prevent="add()">
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
    <div class="grid grid-cols-4 gap-6 mt-16" v-if="nfts">
      <router-link
        class="w-full transition duration-200 transform border-gray-300 rounded-lg  bg-gray-50 hover:scale-105 h-96 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        v-for="(nft, index) in nfts"
        :key="nft.id"
        :index="index"
        :to="'/explore/' + nft.id"
      >
        <div class="flex flex-col p-4">
          <div class="grid grid-cols-2 gap-2">
            <span class="text-sm font-medium">owner</span>
            <span class="text-sm truncate">{{ nft.creator_id }}</span>
            <span class="text-sm font-medium">id</span>
            <span class="text-sm truncate">{{ nft.id }}</span>
            <span class="text-sm font-medium">metadata</span>
            <span class="text-sm truncate">{{ nft.artifact_uri }}</span>
          </div>
        </div>
      </router-link>
    </div>
    <div class="flex items-center justify-between mt-16">
      <div class="flex items-center space-x-2">
        <button
          v-for="i in [1]"
          :key="i"
          class="flex items-center w-10 h-10 p-3 rounded-md hover:bg-gray-100"
          :class="i === 1 ? 'text-white bg-cyan-500 hover:bg-cyan-600' : ''"
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
  <CreateDatasetModal
    :isOpen="isCreateDatasetModalOpen"
    @update:isOpen="isCreateDatasetModalOpen = $event"
  />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
//import { AdjustmentsIcon, SortAscendingIcon } from "@heroicons/vue/outline";
import SearchBar from "@/components/SearchBar.vue";
import CreateDatasetModal from "@/components/Explorer/CreateDatasetModal.vue";
import { useQuery, useResult } from "@vue/apollo-composable";
import { getTokenMetadata } from "@/services/graphql/queries";

export default defineComponent({
  components: {
    //AdjustmentsIcon,
    //SortAscendingIcon,
    CreateDatasetModal,
    SearchBar,
  },
  setup() {
    const isCreateDatasetModalOpen = ref(false);
    // fetches 12 nfts from contract when component mounts
    const { result } = useQuery(getTokenMetadata, () => ({
      offset: 0,
      limit: 12,
    }));
    // stores result in nfts when result is loaded
    const nfts = useResult(result, null, ({token}) => token);

    return { nfts, isCreateDatasetModalOpen };
  },
});
</script>
