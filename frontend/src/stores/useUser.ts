import { defineStore } from "pinia";
import { getBalance, getAddress } from "@/services/wallet-service";

export const useUserStore = defineStore("user", {
  state: () => ({
    address: "" as string | undefined,
    balance: 0 as number | undefined,
  }),
  getters: {
    getAddress: (state) => state.address,
    getBalance: (state) => state.balance,
  },
  actions: {
    async initBalance() {
      try {
        this.balance = await getBalance();
      } catch (e) {
        console.log(e);
        this.balance = 0;
      }
    },
    async initAddress() {
      try {
        this.address = await getAddress();
      } catch (e) {
        console.log(e);
        this.address = "";
      }
    },
  },
});
