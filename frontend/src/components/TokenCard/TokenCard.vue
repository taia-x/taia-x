<template>
  <component
    :is="is"
    class="block w-full h-56 transition duration-200 transform border-2 border-gray-100 rounded-lg hover:shadow-xl hover:-translate-y-2 focus:outline-none focus:ring-2 focus:ring-cyan-500"
    :to="to"
  >
    <div class="flex flex-col justify-between h-full p-4">
      <div>
        <div class="flex items-center justify-between">
          <span class="text-xs text-gray-500">Owner</span>
          <span class="text-xs text-gray-500">Price</span>
        </div>
        <div class="flex items-center justify-between mt-1">
          <span class="flex items-center"
            ><img
              :src="`${ACCOUNT_IMAGE_PATH}${token.creator_id}`"
              class="absolute w-8 h-8 left-2.5"
            />
            <span class="text-sm font-semibold text-gray-900 ml-7">
              {{ getPrivatizedAddress(token.creator_id) }}
            </span></span
          >
          <span class="text-sm font-semibold text-gray-900"
            >{{ token.price / 1000000 }} ꜩ</span
          >
        </div>
        <div class="flex items-center mt-4">
          <span class="font-semibold text-gray-900 truncate"
            >{{ token.name }}
          </span>
        </div>
        <div class="flex items-start mt-2">
          <span class="h-full text-sm text-gray-500 line-clamp-3"
            >{{ token.description }}
          </span>
        </div>
      </div>
      <div class="flex items-center justify-between mt-4">
        <div class="flex items-center space-x-1">
          <LoadingSpinner
            v-if="token?.cert_state === 'pending'"
            :size="5"
            :color="'text-gray-500'"
            class="mr-1"
          />
          <BadgeCheckIcon
            v-if="token?.cert_state === 'certified'"
            class="w-5 h-5 text-gray-500 transform -translate-x-0.5"
          />
          <BanIcon
            v-if="token?.cert_state === 'rejected'"
            class="w-5 h-5 text-gray-500 transform -translate-x-0.5"
          />
          <span class="text-sm font-semibold text-gray-900">{{
            token?.cert_state[0].toUpperCase() + token?.cert_state.slice(1)
          }}</span>
        </div>
        <div class="flex items-center space-x-1">
          <DocumentIcon class="w-5 h-5 text-gray-500" />
          <span class="text-sm font-semibold text-gray-900">{{
            token?.files.length
          }}</span>
        </div>
      </div>
    </div>
  </component>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import LoadingSpinner from "@/components/Utils/LoadingSpinner.vue";
import { ACCOUNT_IMAGE_PATH } from "@/constants";
import { DocumentIcon, BadgeCheckIcon, BanIcon } from "@heroicons/vue/outline";

export default defineComponent({
  components: {
    DocumentIcon,
    BadgeCheckIcon,
    LoadingSpinner,
    BanIcon,
  },
  props: {
    token: {
      type: Object,
      required: true,
    },
    is: {
      type: String,
      default: "router-link",
    },
  },
  setup(props: any) {
    const getPrivatizedAddress = (address: string) => {
      return `${address.substring(0, 5)}...${address.substring(
        address.length - 5,
        address.length
      )}`;
    };

    const to = props.is === "router-link" && "/explore/" + props.token.id;

    return {
      getPrivatizedAddress,
      ACCOUNT_IMAGE_PATH,
      to,
    };
  },
});
</script>
