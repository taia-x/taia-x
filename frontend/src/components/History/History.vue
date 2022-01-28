<template>
  <div
    class="grid grid-cols-5 grid-rows-1 px-3 py-2 font-medium text-gray-900 border-t-2 border-l-2 border-r-2 border-gray-100 rounded-t-lg"
  >
    <div>Event</div>
    <div>From</div>
    <div>To</div>
    <div>Amount</div>
    <div>Date</div>
  </div>
  <div
    class="grid grid-cols-5 grid-rows-1 px-3 py-2 text-base text-gray-700 border-2 border-gray-100"
    :class="
      index >= 1
        ? 'border-t-0'
        : index + 1 === token.events.length
        ? 'rounded-b-lg'
        : ''
    "
    v-for="(event, index) in token.events"
    :key="event.id"
    :index="index"
  >
    <div class="flex items-center space-x-2">
      <DocumentAddIcon
        v-if="event.event_type === 'mint'"
        class="w-5 h-5 text-gray-700"
      />
      <BadgeCheckIcon
        v-if="event.event_type === 'certify'"
        class="w-5 h-5 text-gray-700"
      />
      <ShoppingBagIcon
        v-if="event.event_type === 'purchase'"
        class="w-5 h-5 text-gray-700"
      />
      <BanIcon
        v-if="event.event_type === 'reject'"
        class="w-5 h-5 text-gray-700"
      />
      <SwitchHorizontalIcon
        v-if="event.event_type === 'transfer'"
        class="w-5 h-5 text-gray-700"
      />
      <span class="truncate">
        {{ event.event_type[0].toUpperCase() + event.event_type.slice(1) }}
      </span>
    </div>
    <div v-if="event" class="flex">
      <a
        :href="`https://tzkt.io/${event.caller_id}`"
        target="_blank"
        class="flex items-center space-x-2"
      >
        <img
          v-if="event.caller_id"
          :src="`https://services.tzkt.io/v1/avatars/${event.caller_id}`"
          class="w-10 h-10 my-auto"
        />
        <span class="truncate">{{
          event.caller_id ? getPrivatizedAddress(event.caller_id) : "-"
        }}</span>
      </a>
    </div>
    <div v-if="event" class="flex">
      <a
        target="_blank"
        :href="`https://tzkt.io/${event.recipient_id}`"
        class="flex items-center space-x-2"
      >
        <img
          v-if="event.recipient_id"
          :src="`https://services.tzkt.io/v1/avatars/${event.recipient_id}`"
          class="w-10 h-10 my-auto"
        />
        <span class="truncate">{{
          event.recipient_id ? getPrivatizedAddress(event.recipient_id) : "-"
        }}</span>
      </a>
    </div>
    <div class="flex items-center">
      <span class="truncate">{{
        event.price ? event.price / 1000000 + " ꜩ" : "-"
      }}</span>
    </div>
    <div class="flex items-center">
      <a
        class="truncate"
        target="_blank"
        :href="`https://tzkt.io/${event.ophash}`"
        >{{ new Date(event.timestamp).toDateString() }}</a
      >
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import {
  DocumentAddIcon,
  ShoppingBagIcon,
  BadgeCheckIcon,
  BanIcon,
  SwitchHorizontalIcon,
} from "@heroicons/vue/outline";

export default defineComponent({
  props: {
    token: {
      type: Object,
      required: true,
    },
  },
  components: {
    DocumentAddIcon,
    ShoppingBagIcon,
    BadgeCheckIcon,
    BanIcon,
    SwitchHorizontalIcon,
  },
  setup() {
    const getPrivatizedAddress = (address) => {
      return `${address.substring(0, 5)}...${address.substring(
        address.length - 5,
        address.length
      )}`;
    };

    return { getPrivatizedAddress };
  },
});
</script>
