<script>
import { h, toRefs, watchEffect } from "vue";
import { highlight, languages } from "prismjs";

export default {
  props: {
    code: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const { code } = toRefs(props);
    let renderedCode = null;

    watchEffect(() => {
      renderedCode = highlight(code.value, languages.javascript);
    });

    return () =>
      renderedCode.length
        ? h(
            "pre",
            { class: "flex min-h-full text-xs md:text-sm language-javascript" },
            [
              h(
                "div",
                {
                  class:
                    "flex-none hidden py-4 pr-4 text-right text-white text-opacity-50 select-none md:block",
                  style: "width:50px",
                  id: "rowNumbers",
                  ariaHidden: true,
                },
                [...props.code.match(/\n/g), "\n"].map((_, index) => [
                  h("span", { innerHTML: index + 1 }),
                  h("br"),
                ])
              ),
              h("code", {
                class:
                  "relative flex-auto block px-4 pt-4 pb-4 overflow-auto text-white",
                innerHTML: renderedCode,
              }),
            ]
          )
        : null;
  },
};
</script>
