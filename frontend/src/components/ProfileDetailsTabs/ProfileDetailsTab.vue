<template>
  <div class="grid grid-cols-4 gap-6" v-if="loading">
    <TokenCardSkeleton
      class="w-full h-56 transition duration-200 border-2 border-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500"
      v-for="i in 10"
      :key="i"
      :index="i"
    />
  </div>
  <div class="grid grid-cols-4 gap-6" v-if="!loading">
    <span
      v-if="!tokens.length"
      class="absolute w-full text-sm font-semibold text-center text-gray-700"
      ><slot></slot
    ></span>
    <TokenCard v-for="token in tokens" :key="token.id" :token="token" />
  </div>
</template>

<script>
import { defineComponent } from "vue";
import TokenCard from "@/components/TokenCard/TokenCard.vue";
import TokenCardSkeleton from "@/components/TokenCard/TokenCardSkeleton.vue";

export default defineComponent({
  components: {
    TokenCard,
    TokenCardSkeleton,
  },
  props: {
    tokens: {
      type: [null, Array],
      required: true,
    },
    loading: {
      type: Boolean,
      required: true,
    },
  },
});
</script>
