/* eslint @typescript-eslint/no-var-requires: "off" */
const openInEditor = require("launch-editor-middleware");

module.exports = {
  devServer: {
    disableHostCheck: true,
    setup(app) {
      app.use("/__open-in-editor", openInEditor("code"));
    },
    public: "http://localhost:8080",
  },
  // configureWebpack: {
  //   performance: {
  //     hints: false,
  //   },
  //   optimization: {
  //     splitChunks: {
  //       minSize: 10000,
  //       maxSize: 250000,
  //     },
  //   },
  // },
};
