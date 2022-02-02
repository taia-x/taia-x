<template>
  <div v-if="events && events.length">
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

    const { result } = useQuery(
      getEventsByAccount,
      {
        accountId: address,
      },
      {
        fetchPolicy: "cache-and-network",
      }
    );
    const events = useResult(result, null, ({ event }) => event);

    return {
      route,
      events,
      address,
    };
  },
});
</script>
