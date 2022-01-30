<template>
  <Terminal
    :code="code"
    :file="selected"
    :token="token"
    class="mt-10 filter drop-shadow-2xl"
  />
  <div v-if="token">
    <Header :token="token" />
    <BuyButton :token="token" />
    <div class="flex flex-col pt-12 pb-20 space-y-12">
      <Section
        ><template #title>Description</template
        ><template #content
          ><p class="text-base text-gray-700">
            {{ token.description }}
          </p></template
        ></Section
      >
      <Section
        ><template #title>Attributes</template
        ><template #content
          ><p class="text-base text-gray-700">
            {{ token.description }}
          </p></template
        ></Section
      >
      <Section
        ><template #title>Files</template
        ><template #content
          ><FileList
            :files="token.files"
            @update:selected="selected = $event"
            @update:code="code = $event" /></template
      ></Section>
      <Section
        ><template #title>History</template
        ><template #content
          ><div><History :events="events" /></div></template
      ></Section>
    </div>
    <div class="space-y-4" v-if="token && token.files">
      <h3
        class="flex items-center space-x-1 text-xl font-semibold text-gray-900"
      >
        <span>Files</span>
        <InformationCircleIcon
          class="w-5 h-5 text-gray-400 transform -translate-y-1"
        />
      </h3>
      <div
        class="flex items-center justify-between w-full p-2 mt-1 bg-gray-100 rounded-md"
        v-for="file in token.files"
        :key="file.fileName"
      >
        <div class="flex items-center space-x-2">
          <DocumentTextIcon class="w-5 h-5 text-gray-700" />
          <span class="font-mono truncate">{{ file.fileName }}</span>
        </div>
        <div class="flex items-center space-x-4">
          <span class="font-mono">{{ file.fileSize }} Byte</span>
          <Tooltip
            class="group"
            @click.prevent="fetchPreview(file)"
            v-if="file.previewUri"
          >
            <template #element
              ><EyeIcon
                class="w-5 h-5 text-gray-400 transition-colors duration-150 hover:text-gray-700"
            /></template>
            <template #text>Show Preview</template>
          </Tooltip>
        </div>
      </div>
    </div>
    <div v-if="token">
      <History :token="token.events" />
    </div>
  </div>
</template>

<script>
import { defineComponent, watchEffect, ref, watch, onUnmounted } from "vue";
import Terminal from "@/components/Utils/Terminal.vue";
import History from "@/components/History/History.vue";
import Header from "@/components/ExplorerDetails/Header.vue";
import BuyButton from "@/components/ExplorerDetails/BuyButton.vue";
import Section from "@/components/ExplorerDetails/Section.vue";
import FileList from "@/components/ExplorerDetails/FileList.vue";
import { useRoute } from "vue-router";
import { ipfsInterface } from "@/services";
import { useQuery, useResult, useSubscription } from "@vue/apollo-composable";
import {
  getSingleTokenMetadata,
  subscribeToTokenEvent,
} from "@/services/graphql/queries";

export default defineComponent({
  components: {
    Terminal,
    History,
    Header,
    BuyButton,
    Section,
    FileList,
  },
  setup() {
    const route = useRoute();
    const code = ref("");
    const token = ref(null);
    const selected = ref({});
    const events = ref([]);
    const enabled = ref(true);

    // fetches single token metadata based on route param
    const { result } = useQuery(getSingleTokenMetadata, () => ({
      id: Number(route.params.id),
    }));

    // gets token metadata when result is loaded
    const token_metadata = useResult(
      result,
      null,
      ({ token_by_pk }) => token_by_pk
    );

    // render ui when token_metadata contains values
    watchEffect(async () => {
      if (token_metadata?.value?.id) {
        selected.value = token_metadata.value.files[0];
        token.value = token_metadata.value;
        if (token_metadata.value.files) {
          const file = token_metadata.value.files.find(
            (file) => file.previewUri !== null
          );
          if (file) {
            const asset = await fetch(
              ipfsInterface.makeGatewayURL(file.previewUri)
            );
            code.value = JSON.stringify(await asset.json(), null, 2);
          }
        }
      }
    });

    // subscribe to new token events
    const subscription = useSubscription(
      subscribeToTokenEvent,
      () => ({
        token_id: Number(route.params.id),
      }),
      () => ({
        enabled: enabled.value,
        fetchPolicy: "cache-and-network",
      })
    );

    // watch for new token events and update events
    watch(
      subscription.result,
      (data) => {
        events.value = data.event;
      },
      {
        lazy: true,
      }
    );

    // unsubscribe to new token events on unmounted
    onUnmounted(() => {
      enabled.value = false;
    });

    return {
      code,
      selected,
      route,
      events,
      token,
    };
  },
});
</script>
