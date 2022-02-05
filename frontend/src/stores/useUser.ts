import { defineStore } from "pinia";
import { walletInterface } from "@/services/index";

export const useUserStore = defineStore("user", {
  // initial state of user
  state: () => ({
    address: "",
    pbkey: "",
    balance: 0,
    role: "",
  }),
  actions: {
    /**
     * function to set address and balance of user in pinia store
     */
    async initializeUser() {
      try {
        const account = await walletInterface.getAccount();
        this.address = account.address;
        this.pbkey = account.publicKey;
      } catch (e: any) {
        throw new Error(e.toString());
      }
    },
  },
});
