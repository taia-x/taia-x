import { defineStore } from "pinia";
import { walletInterface } from "@/services/index";

export const useUserStore = defineStore("user", {
  // initial state of user
  state: () => ({
    address: "",
    balance: 0,
    role: "",
  }),
  actions: {
    /**
     * function to set address and balance of user in pinia store
     */
    async initializeUser() {
      try {
        const address = await walletInterface.getAddress();
        this.address = address;
      } catch (e: any) {
        throw new Error(e.toString());
      }
    },
  },
});
