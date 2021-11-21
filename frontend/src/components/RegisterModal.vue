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
              class="inline-block w-full max-w-md p-6 my-8 overflow-hidden text-left align-middle transition-all transform bg-white shadow-xl  rounded-2xl"
            >
              <DialogTitle
                as="h3"
                class="text-lg font-medium leading-6 text-gray-900"
              >
                Choose your role
              </DialogTitle>
              <div class="mt-6">
                <ul
                  class="grid grid-cols-1 gap-4 sm:grid-cols-1 lg:grid-cols-3"
                >
                  <li
                    class="rounded-lg  hover:shadow-lg bg-gradient-to-br hover:from-cyan-400 hover:to-light-blue-500 hover:text-gray-50"
                  >
                    <a
                      href="#"
                      class="flex items-center justify-center w-full py-4 text-sm font-medium border-2 border-gray-200 border-dashed rounded-lg  hover:border-transparent"
                    >
                      Certifier
                    </a>
                  </li>
                  <li
                    class="rounded-lg  hover:shadow-lg bg-gradient-to-br hover:from-yellow-400 hover:to-orange-500 hover:text-gray-50"
                  >
                    <a
                      href="#"
                      class="flex items-center justify-center w-full py-4 text-sm font-medium border-2 border-gray-200 border-dashed rounded-lg  hover:border-transparent"
                    >
                      Provider
                    </a>
                  </li>
                  <li
                    class="rounded-lg  hover:shadow-lg bg-gradient-to-br hover:from-pink-400 hover:to-rose-500 hover:text-gray-50"
                  >
                    <a
                      href="#"
                      class="flex items-center justify-center w-full py-4 text-sm font-medium border-2 border-gray-200 border-dashed rounded-lg  hover:border-transparent"
                    >
                      Consumer
                    </a>
                  </li>
                </ul>
              </div>

              <!-- <div class="mt-4">
                <button
                  type="button"
                  class="inline-flex justify-center px-4 py-2 text-sm font-medium text-blue-900 bg-blue-100 border border-transparent rounded-md hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-500"
                  @click="$emit('update:isOpen', false)"
                >
                  Got it, thanks!
                </button>
              </div> -->
            </div>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
  Dialog,
  DialogOverlay,
  //DialogTitle,
  TransitionRoot,
  TransitionChild,
} from "@headlessui/vue";

export default defineComponent({
  components: {
    Dialog,
    DialogOverlay,
    //DialogTitle,
    TransitionRoot,
    TransitionChild,
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
