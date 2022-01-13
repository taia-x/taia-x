/* eslint @typescript-eslint/no-var-requires: "off" */
const colors = require("tailwindcss/colors");
const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  //mode: "jit",
  purge: ["./public/**/*.html", "./src/**/*.{js,jsx,ts,tsx,vue}"],
  darkMode: "class", // false or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter var", ...defaultTheme.fontFamily.sans],
        mono: ["Menlo", ...defaultTheme.fontFamily.mono],
        source: ["Source Sans Pro", ...defaultTheme.fontFamily.sans],
        "ubuntu-mono": ["Ubuntu Mono", ...defaultTheme.fontFamily.mono],
        system: defaultTheme.fontFamily.sans,
      },
      colors: {
        gray: colors.gray,
        cyan: colors.cyan,
        fuchsia: colors.fuchsia,
        sky: colors.sky,
        lime: colors.lime,
        rose: colors.rose,
        emerald: colors.emerald,
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
      borderStyle: ["hover"],
      backgroundOpacity: ["hover"],
      backgroundColor: ["disabled"],
      textColor: ["disabled"],
      cursor: ["disabled"],
      fontWeight: ["hover", "focus"],
    },
    translate: ({ after }) => after(["group-hover"]),
  },
  plugins: [require("@tailwindcss/forms")],
};
