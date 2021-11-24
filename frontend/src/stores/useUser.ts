import { defineStore } from "pinia";
import { tezosInterface } from "@/services/index";

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
    async initializeUser() {
      try {
        const [address, balance] = await Promise.all([
          tezosInterface.getAddress(),
          tezosInterface.getBalance(),
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
