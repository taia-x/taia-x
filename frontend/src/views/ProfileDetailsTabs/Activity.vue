<template>
  <div :class="['py-8']" v-if="events">
    <History :events="events" />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { useRoute } from "vue-router";
import { getEventsByAccount } from "@/services/graphql/queries";
import { useQuery, useResult } from "@vue/apollo-composable";
import History from "@/components/History/History.vue";

export default defineComponent({
  components: {
    History,
  },
  setup() {
    const route = useRoute();
    const address = route.params.address;

    const { result } = useQuery(getEventsByAccount, {
      accountId: address,
    });
    const events = useResult(result, null, ({ event }) => event);

    return {
      route,
      events,
      address,
    };
  },
});
</script>
