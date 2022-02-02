<template>
  <div class="container pt-10 mx-auto space-y-6">
    <div class="flex items-center space-x-3">
      <img :src="`${ACCOUNT_IMAGE_PATH}${address}`" class="w-16 h-16" />
      <a
        :href="`https://tzkt.io/${address}`"
        target="_blank"
        class="font-semibold text-gray-700"
      >
        {{
          `${address.substring(0, 5)}...${address.substring(
            address.length - 5,
            address.length
          )}`
        }}
      </a>
    </div>
    <div>
      <nav class="flex space-x-10 border-b-2 border-gray-100">
        <router-link
          v-for="title in tabs"
          :key="title"
          :to="title.toLowerCase()"
          v-slot="{ isExactActive }"
        >
          <div
            :class="[
              'relative flex items-center',
              title === 'certified' &&
                user.role !== 'certifier' &&
                'cursor-not-allowed',
            ]"
          >
            <LockClosedIcon
              class="w-5 h-5 mr-1 text-gray-300"
              v-if="title === 'certified' && user.role !== 'certifier'"
            />
            <div
              :class="[
                'py-4 text-gray-300 font-semibold transition duration-150 ease-in-out capitalize',
                isExactActive && 'text-gray-900',
                title === 'certified' && user.role !== 'certifier'
                  ? ''
                  : 'hover:text-gray-900',
              ]"
            >
              {{ title }}
            </div>
            <span
              aria-hidden="true"
              :class="[
                'absolute w-full h-0.5 -bottom-0.5 left-0 transition duration-150 ease-in-out',
                isExactActive ? 'bg-cyan-500' : 'bg-transparent',
              ]"
            ></span>
          </div>
        </router-link>
      </nav>
      <div class="py-8 mt-2">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from "vue";
import { useRoute } from "vue-router";
import { ACCOUNT_IMAGE_PATH } from "@/constants";
import { LockClosedIcon } from "@heroicons/vue/outline";
import { useUserStore } from "@/stores/useUser";

export default defineComponent({
  components: {
    LockClosedIcon,
  },
  setup() {
    const route = useRoute();
    const user = useUserStore();

    const address = computed(() => route.params.address);

    const tabs = ["collected", "created", "certified", "activity"];

    return {
      route,
      tabs,
      user,
      ACCOUNT_IMAGE_PATH,
      address,
    };
  },
});
</script>
