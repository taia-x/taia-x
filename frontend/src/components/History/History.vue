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
        : index + 1 === events.length
        ? 'rounded-b-lg'
        : ''
    "
    v-for="(event, index) in events"
    :key="event.id"
    :index="index"
  >
    <div class="flex items-center space-x-2">
      <component :is="type(event)" class="w-5 h-5 text-gray-700" />
      <span class="truncate">
        {{ event.event_type[0].toUpperCase() + event.event_type.slice(1) }}
      </span>
    </div>
    <div v-if="event" class="flex">
      <div
        @click.prevent="$router.push(`/profile/${event._from_id}`)"
        class="flex items-center space-x-2 cursor-pointer"
      >
        <img
          v-if="event._from_id"
          :src="`https://services.tzkt.io/v1/avatars/${event._from_id}`"
          class="w-10 h-10 my-auto"
        />
        <span class="truncate">{{
          event._from_id ? getPrivatizedAddress(event._from_id) : "-"
        }}</span>
      </div>
    </div>
    <div v-if="event" class="flex">
      <div
        @click.prevent="$router.push(`/profile/${event._to_id}`)"
        class="flex items-center space-x-2 cursor-pointer"
      >
        <img
          v-if="event._to_id"
          :src="`https://services.tzkt.io/v1/avatars/${event._to_id}`"
          class="w-10 h-10 my-auto"
        />
        <span class="truncate">{{
          event._to_id ? getPrivatizedAddress(event._to_id) : "-"
        }}</span>
      </div>
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
    events: {
      type: Array,
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
  setup(props) {
    const getPrivatizedAddress = (address) => {
      return `${address.substring(0, 5)}...${address.substring(
        address.length - 5,
        address.length
      )}`;
    };

    const type = (event) => {
      if (event.event_type === "mint") return "DocumentAddIcon";
      if (event.event_type === "certify") return "BadgeCheckIcon";
      if (event.event_type === "purchase") return "ShoppingBagIcon";
      if (event.event_type === "reject") return "BanIcon";
      else return "SwitchHorizontalIcon";
    };

    return { type, getPrivatizedAddress };
  },
});
</script>
