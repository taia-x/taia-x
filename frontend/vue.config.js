/* eslint @typescript-eslint/no-var-requires: "off" */
const openInEditor = require("launch-editor-middleware");

module.exports = {
  devServer: {
    setup(app) {
      app.use("/__open-in-editor", openInEditor("code"));
    },
    host: "0.0.0.0", // to accept connections from outside container
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "*",
    },
    proxy: {
      "/api": {
        target: "http://taia-x-backend:8000",
      },
    },
    watchOptions: {
      aggregateTimeout: 500, // delay before reloading
      poll: 1000, // enable polling since fsevents are not supported in docker
    },
  },
  configureWebpack: {
    performance: {
      hints: false,
    },
    optimization: {
      splitChunks:
        process.env.NODE_ENV === "production"
          ? {
              minSize: 10000,
              maxSize: 250000,
            }
          : undefined,
    },
  },
};
