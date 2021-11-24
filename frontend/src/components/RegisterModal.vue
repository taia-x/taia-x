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
                Choose your role
              </DialogTitle>
              <div class="mt-6 text-gray-700">
                <ul
                  class="grid grid-cols-1 gap-4 sm:grid-cols-1 lg:grid-cols-3"
                >
                  <li
                    class="transition duration-300 ease-in-out border-2 border-gray-200 border-dashed rounded-lg  hover:border-transparent hover:bg-purple-100 hover:text-purple-800"
                  >
                    <a
                      href="#"
                      class="flex items-center justify-center w-full py-4 space-x-2 text-sm font-medium  group"
                    >
                      <LibraryIcon
                        class="w-5 h-5 text-gray-600 transition duration-300 ease-in-out  group-hover:text-purple-600"
                      />
                      <span>Certifier</span>
                    </a>
                  </li>
                  <li
                    class="transition duration-300 ease-in-out border-2 border-gray-200 border-dashed rounded-lg  hover:border-transparent hover:bg-purple-100 hover:text-purple-800"
                  >
                    <a
                      href="#"
                      class="flex items-center justify-center w-full py-4 space-x-2 text-sm font-medium  group"
                    >
                      <BriefcaseIcon
                        class="w-5 h-5 text-gray-600 transition duration-300 ease-in-out  group-hover:text-purple-600"
                      />
                      <span>Provider</span>
                    </a>
                  </li>
                  <li
                    class="transition duration-300 ease-in-out border-2 border-gray-200 border-dashed rounded-lg  hover:border-transparent hover:bg-purple-100 hover:text-purple-800"
                  >
                    <a
                      href="#"
                      class="flex items-center justify-center w-full py-4 space-x-2 text-sm font-medium  group"
                    >
                      <ShoppingBagIcon
                        class="w-5 h-5 text-gray-600 transition duration-300 ease-in-out  group-hover:text-purple-600"
                      />
                      <span>Consumer</span>
                    </a>
                  </li>
                </ul>
              </div>
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
  LibraryIcon,
  BriefcaseIcon,
  ShoppingBagIcon,
} from "@heroicons/vue/outline";
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
    LibraryIcon,
    BriefcaseIcon,
    ShoppingBagIcon,
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
