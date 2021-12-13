import { defineStore } from "pinia";
import { walletInterface } from "@/services/index";

export const useUserStore = defineStore("user", {
  // initial state of user
  state: () => ({
    address: "",
    balance: 0,
  }),
  getters: {
    getAddress: (state) => state.address,
    getBalance: (state) => state.balance,
  },
  actions: {
    /**
     * function to set address and balance of user in pinia store
     */
    async initializeUser() {
      try {
        const [address, balance] = await Promise.all([
          walletInterface.getAddress(),
          walletInterface.getBalance(),
        ]);
        this.address = address;
        this.balance = balance;
      } catch (e) {
        console.log(e);
        this.balance = 0;
        this.address = "";
      }
    },
  },
});
