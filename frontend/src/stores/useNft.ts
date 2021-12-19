import { defineStore } from "pinia";

export const useNftStore = defineStore("nfts", {
  // initial state of nfts
  state: () => ({
    nfts: [] as Array<any>,
  }),
  getters: {
    getOntologies: (state) => state.nfts,
  },
});
