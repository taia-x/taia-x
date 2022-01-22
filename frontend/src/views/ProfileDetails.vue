<template>
  <div
    class="
      container mx-auto
    "
  >
    <span class="text-xl">Account: {{ route.params.address }}</span>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { useRoute } from "vue-router";

export default defineComponent({
  components: {},
  setup() {
    const route = useRoute();

    return {
      route,
    };
  },
});
</script>
