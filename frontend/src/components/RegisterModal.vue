<template>
  <Modal :isOpen="isOpen" @update:isOpen="$emit('update:isOpen', $event)">
    <template #title>Choose your role</template>
    <template #content><RegisterModalContent /></template>
  </Modal>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import RegisterModalContent from "@/components/RegisterModalContent.vue";
import Modal from "@/components/Utils/Modal.vue";

export default defineComponent({
  components: {
    Modal,
    RegisterModalContent,
  },
  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },
  },
});
</script>

<style></style>
