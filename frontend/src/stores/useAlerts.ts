import { defineStore } from "pinia";
import { Alert } from "@/types";

export const useAlertStore = defineStore("alerts", {
  // initial state of alerts
  state: () => ({
    alerts: [] as Array<Alert>,
    counter: 0,
  }),
  getters: {
    getAlerts: (state) => state.alerts,
  },
  actions: {
    // adds alert to alerts array and automatically removes it after 4s
    createAlert(message: string, type = "info"): void {
      const index = this.alerts.length;

      this.alerts.push({
        id: this.counter++,
        message,
        type,
        visible: true,
      } as Alert);

      setTimeout(() => {
        this.destroyAlert(index);
      }, 4000);
    },

    // sets visibility of alert to false
    destroyAlert(index: number): void {
      this.alerts[index].visible = false;
    },
  },
});
