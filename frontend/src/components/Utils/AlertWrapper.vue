<template>
  <div
    class="fixed top-0 left-0 z-50 flex flex-col ml-10 space-y-4 transition-all duration-200 transform  mt-28"
  >
    <Alert
      v-for="(alert, index) in alerts"
      :key="index"
      :index="index"
      :alert="alert"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Alert from "@/components/Utils/Alert.vue";
import { useAlertStore } from "@/stores/useAlerts";
import { storeToRefs } from "pinia";

export default defineComponent({
  components: {
    Alert,
  },
  setup() {
    const alertStore = useAlertStore();
    const { alerts } = storeToRefs(alertStore);
    return { alerts };
  },
});
</script>
