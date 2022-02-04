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
          <LoadingSpinner
            v-if="token?.cert_state === 'pending'"
            :size="5"
            :color="'text-gray-400'"
            class="mr-1"
          />
          <BadgeCheckIcon
            v-if="token?.cert_state === 'certified'"
            class="w-5 h-5"
          />
          <BanIcon v-if="token?.cert_state === 'rejected'" class="w-5 h-5" />
          <span>{{
            token?.cert_state[0].toUpperCase() + token?.cert_state.slice(1)
          }}</span>
        </div>
      </div>
    </div>
    <div
      v-if="token && token.creator_id"
      @click.prevent="$router.push(`/profile/${token?.creator_id}`)"
      class="z-10 flex items-center space-x-2 cursor-pointer"
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
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { DocumentIcon, BadgeCheckIcon, BanIcon } from "@heroicons/vue/outline";
import LoadingSpinner from "@/components/Utils/LoadingSpinner.vue";

export default defineComponent({
  components: {
    DocumentIcon,
    BadgeCheckIcon,
    BanIcon,
    LoadingSpinner,
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
