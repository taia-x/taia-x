/* eslint @typescript-eslint/no-var-requires: "off" */
const colors = require("tailwindcss/colors");

module.exports = {
  mode: "jit",
  purge: ["./public/**/*.html", "./src/**/*.{js,jsx,ts,tsx,vue}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        background: "#121212",
        custom: {
          secondary: "rgba(25, 27, 31, 0.6)",
          "secondary-notrans": "rgb(25, 27, 31)",
          tertiary: "#25272C",
          background: "#1F2128",
          lines: "#1D1E23",
        },
        gray: colors.gray,
      },

      animation: {
        pulse: "pulse 1.5s cubic-bezier(0.4, 0, 0.6, 1) infinite",
      },

      keyframes: {
        pulse: {
          "0%, 100%": {
            opacity: 0,
          },
          "50%": {
            opacity: 1,
          },
        },
      },
      transitionProperty: {
        height: "height",
      },
    },
  },
  variants: {
    extend: {
      ringWidth: ["focus-visible"],
      ringColor: ["focus-visible"],
      ringOffsetWidth: ["focus-visible"],
      ringOffsetColor: ["focus-visible"],
    },
  },
  plugins: [],
};
