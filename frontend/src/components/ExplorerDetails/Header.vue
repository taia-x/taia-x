<template>
  <div class="flex items-center justify-between pt-10 pb-4">
    <div v-if="token && token.files">
      <h1 class="text-3xl font-extrabold tracking-tight text-gray-800">
        {{ token?.name }}
      </h1>
      <div class="flex items-center mt-1 space-x-4 text-xl text-gray-400">
        <div># {{ token.id }}</div>
        <div class="flex items-center space-x-1">
          <DocumentIcon class="w-5 h-5" />
          <span>{{ token?.files.length }} Files</span>
        </div>
        <div class="flex items-center space-x-1">
          <ClockIcon class="w-5 h-5" />
          <span>30s</span>
        </div>
      </div>
    </div>
    <a
      v-if="token && token.creator_id"
      :href="`https://tzkt.io/${token?.creator_id}`"
      target="_blank"
      class="z-10 flex items-center space-x-2"
    >
      <div class="flex flex-col">
        <div class="font-medium text-right text-gray-700">Owner</div>
        <div class="pb-2 text-sm font-medium text-right text-gray-400">
          {{ getPrivatizedAddress(token?.creator_id) }}
        </div>
      </div>
      <img
        :src="`https://services.tzkt.io/v1/avatars/${token?.creator_id}`"
        class="w-16 h-16 my-auto"
      />
    </a>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { ClockIcon, DocumentIcon } from "@heroicons/vue/outline";

export default defineComponent({
  components: {
    ClockIcon,
    DocumentIcon,
  },
  props: {
    token: {
      type: Object,
      required: true,
    },
  },
  setup() {
    const getPrivatizedAddress = (address) => {
      return `${address.substring(0, 5)}...${address.substring(
        address.length - 5,
        address.length
      )}`;
    };

    return {
      getPrivatizedAddress,
    };
  },
});
</script>
