import { defineStore } from "pinia";

export const useNftStore = defineStore("nfts", {
  // initial state of user
  state: () => ({
    nfts: [] as Array<any>,
  }),
  getters: {
    getOntologies: (state) => state.nfts,
  },
});
