<template>
  <Header
    @update:isOpen="isRegisterModalOpen = $event"
    class="fixed top-0 z-10 bg-white"
  />
  <div class="h-24"></div>
  <div class="relative w-full max-w-6xl mx-auto">
    <router-view
      @update:isCreateDatasetModalOpen="isCreateDatasetModalOpen = $event"
      @update:isCreateOntologyModalOpen="isCreateOntologyModalOpen = $event"
    />
  </div>
  <RegisterModal
    :isOpen="isRegisterModalOpen"
    @update:isOpen="isRegisterModalOpen = $event"
  />
  <CreateDatasetModal
    :isOpen="isCreateDatasetModalOpen"
    @update:isOpen="isCreateDatasetModalOpen = $event"
  />
  <CreateOntologyModal
    :isOpen="isCreateOntologyModalOpen"
    @update:isOpen="isCreateOntologyModalOpen = $event"
  />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Header from "@/components/Header.vue";
import RegisterModal from "@/components/RegisterModal.vue";
import CreateDatasetModal from "@/components/CreateDatasetModal.vue";
import CreateOntologyModal from "@/components/CreateOntologyModal.vue";

export default defineComponent({
  components: {
    RegisterModal,
    CreateDatasetModal,
    CreateOntologyModal,
    Header,
  },
  setup() {
    const isRegisterModalOpen = ref(false);
    const isCreateDatasetModalOpen = ref(false);
    const isCreateOntologyModalOpen = ref(false);

    return {
      isRegisterModalOpen,
      isCreateDatasetModalOpen,
      isCreateOntologyModalOpen,
    };
  },
});
</script>
