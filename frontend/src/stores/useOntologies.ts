import { defineStore } from "pinia";

export const useOntologyStore = defineStore("ontologies", {
  // initial state of ontologies
  state: () => ({
    ontologies: [] as Array<any>,
  }),
  getters: {
    getOntologies: (state) => state.ontologies,
  },
});
