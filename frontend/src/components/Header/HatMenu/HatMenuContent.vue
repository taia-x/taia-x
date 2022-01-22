<template>
  <div class="flex flex-col items-center p-1.5 w-48">
    <div class="grid grid-cols-1 space-y-1.5 text-gray-700 w-full">
      <div class="border-b-2">
        <button
          @click.prevent="assignRole(ROLE_PROVIDER)"
          class="w-full font-medium relative flex items-center justify-center px-12 py-2 mb-1.5 text-center rounded-md cursor-pointer hover:bg-gray-100 space-x-2"
        >
          <BriefcaseIcon class="absolute w-5 h-5 left-2" />
          {{ ROLE_PROVIDER[0].toUpperCase() + ROLE_PROVIDER.slice(1) }}
          <div
            v-if="role && role === ROLE_PROVIDER.toLowerCase()"
            class="absolute w-1.5 h-1.5 bg-gray-700 rounded-full right-2"
          ></div>
        </button>
      </div>
      <div>
        <button
          @click.prevent="assignRole(ROLE_CONSUMER)"
          class="relative flex justify-center w-full px-12 py-2 font-medium text-center rounded-md cursor-pointer hover:bg-gray-100"
        >
          <ShoppingBagIcon class="absolute w-5 h-5 left-2" />
          {{ ROLE_CONSUMER[0].toUpperCase() + ROLE_CONSUMER.slice(1) }}
          <div
            v-if="role && role === ROLE_CONSUMER.toLowerCase()"
            class="absolute w-1.5 h-1.5 bg-gray-700 rounded-full right-2"
          ></div>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useUserStore } from "@/stores/useUser";
import { tezosInterface } from "@/services/index";
import { ROLE_PROVIDER, ROLE_CONSUMER } from "@/constants";
import { BriefcaseIcon, ShoppingBagIcon } from "@heroicons/vue/outline";
import { useAlertStore } from "@/stores/useAlerts";
import { storeToRefs } from "pinia";

export default defineComponent({
  components: {
    BriefcaseIcon,
    ShoppingBagIcon,
  },
  setup() {
    const user = useUserStore();
    const alerts = useAlertStore();
    const { address, role } = storeToRefs(user);
    const isOpen = ref(false);

    // assigns a role to a user with transaction on contract
    const assignRole = async (role: string) => {
      try {
        // calls entrypoint on contract
        await tezosInterface.manageRoles([
          {
            add_role: {
              user: address.value,
              role: { [role]: true },
            },
          },
        ]);
        user.$patch((state) => (state.role = role));
        alerts.createAlert(`Successfully registered as ${role}!`, "success");
      } catch (e: any) {
        // error handling
        alerts.createAlert("Something went wrong!", "error");
        throw new Error(e.toString());
      }
    };

    return { isOpen, assignRole, ROLE_PROVIDER, ROLE_CONSUMER, role };
  },
});
</script>
