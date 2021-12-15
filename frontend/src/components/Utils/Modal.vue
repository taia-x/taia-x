<template>
  <TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="$emit('update:isOpen', false)">
      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div class="min-h-screen px-4 text-center">
          <TransitionChild
            as="template"
            enter="duration-300 ease-out"
            enter-from="opacity-0"
            enter-to="opacity-100"
            leave="duration-200 ease-in"
            leave-from="opacity-100"
            leave-to="opacity-0"
          >
            <DialogOverlay class="fixed inset-0 bg-black bg-opacity-30" />
          </TransitionChild>

          <span class="inline-block h-screen align-middle" aria-hidden="true">
            &#8203;
          </span>

          <TransitionChild
            as="template"
            enter="delay-100 duration-300 ease-out"
            enter-from="opacity-0 scale-95"
            enter-to="opacity-100 scale-100"
            leave="delay-100 duration-200 ease-in"
            leave-from="opacity-100 scale-100"
            leave-to="opacity-0 scale-95"
          >
            <div
              class="inline-block w-full max-w-3xl p-6 my-8 overflow-hidden text-left align-middle transition-all transform bg-white shadow-xl  rounded-2xl"
            >
              <DialogTitle
                as="h3"
                class="text-lg font-medium leading-6 text-gray-900"
              >
                <slot name="title"></slot>
              </DialogTitle>
              <div class="mt-8">
                <form>
                  <div class="sm:rounded-md">
                    <div class="space-y-6 bg-white">
                      <slot name="content"></slot>
                    </div>
                    <div
                      class="w-full mt-6 space-x-2 text-right"
                      v-if="hasActions"
                    >
                      <slot name="actions"></slot>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
import {
  Dialog,
  DialogOverlay,
  DialogTitle,
  TransitionRoot,
  TransitionChild,
} from "@headlessui/vue";

export default defineComponent({
  components: {
    Dialog,
    DialogOverlay,
    DialogTitle,
    TransitionRoot,
    TransitionChild,
  },
  props: {
    isOpen: {
      type: Boolean,
      required: true,
    },
  },
  setup(_, { slots }) {
    const hasActions = computed(() => {
      return !!slots.actions;
    });

    return { hasActions };
  },
});
</script>
