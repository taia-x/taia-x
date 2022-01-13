<template>
  <div class="mt-6 text-gray-700">
    <ul class="grid grid-cols-1 gap-4 sm:grid-cols-1 lg:grid-cols-3">
      <li
        class="transition duration-300 ease-in-out border-2 border-gray-200 border-dashed rounded-lg  hover:border-transparent hover:bg-purple-100 hover:text-purple-800"
      >
        <button
          class="flex items-center justify-center w-full py-4 space-x-2 text-sm font-medium  group"
          @click.prevent="assignRole(ROLE_CERTIFIER)"
        >
          <LibraryIcon
            class="w-5 h-5 text-gray-600 transition duration-300 ease-in-out  group-hover:text-purple-600"
          />
          <span>Certifier</span>
        </button>
      </li>
      <li
        class="transition duration-300 ease-in-out border-2 border-gray-200 border-dashed rounded-lg  hover:border-transparent hover:bg-purple-100 hover:text-purple-800"
      >
        <button
          class="flex items-center justify-center w-full py-4 space-x-2 text-sm font-medium  group"
          @click.prevent="assignRole(ROLE_PROVIDER)"
        >
          <BriefcaseIcon
            class="w-5 h-5 text-gray-600 transition duration-300 ease-in-out  group-hover:text-purple-600"
          />
          <span>Provider</span>
        </button>
      </li>
      <li
        class="transition duration-300 ease-in-out border-2 border-gray-200 border-dashed rounded-lg  hover:border-transparent hover:bg-purple-100 hover:text-purple-800"
      >
        <button
          class="flex items-center justify-center w-full py-4 space-x-2 text-sm font-medium  group"
          @click.prevent="assignRole(ROLE_CONSUMER)"
        >
          <ShoppingBagIcon
            class="w-5 h-5 text-gray-600 transition duration-300 ease-in-out  group-hover:text-purple-600"
          />
          <span>Consumer</span>
        </button>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { tezosInterface, walletInterface } from "@/services/index";
import { ROLE_CERTIFIER, ROLE_PROVIDER, ROLE_CONSUMER } from "@/constants";
import {
  LibraryIcon,
  BriefcaseIcon,
  ShoppingBagIcon,
} from "@heroicons/vue/outline";
import { useUserStore } from "@/stores/useUser";
import { useAlertStore } from "@/stores/useAlerts";
import { storeToRefs } from "pinia";

export default defineComponent({
  components: {
    LibraryIcon,
    BriefcaseIcon,
    ShoppingBagIcon,
  },
  setup(_, { emit }) {
    const user = useUserStore();
    const alerts = useAlertStore();
    const { address } = storeToRefs(user);
    const { initializeUser } = user;

    // assigns a role to a user with transaction on contract
    const assignRole = async (role: string) => {
      try {
        await walletInterface.connectWallet();
        await initializeUser();
        // calls entrypoint on contract
        await tezosInterface.manageRoles([
          {
            add_role: {
              user: address.value,
              role: { [role]: true },
            },
          },
        ]);
        // closes modal and notifies user
        emit("update:isOpen", false);
        alerts.createAlert(`Successfully registered as ${role}!`, "success");
      } catch (e: any) {
        // error handling
        alerts.createAlert("Something went wrong!", "error");
        await walletInterface.disconnectWallet();
        await user.$reset();
        throw new Error(e.toString());
      }
    };

    return { assignRole, ROLE_CERTIFIER, ROLE_PROVIDER, ROLE_CONSUMER };
  },
});
</script>

<style></style>
