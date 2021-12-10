import { defineStore } from "pinia";

export const useOntologiesStore = defineStore("ontologies", {
  // initial state of user
  state: () => ({
    ont: [] as Array<any>,
  }),
  getters: {
    getOntologies: (state) => state.ont,
  },
});
