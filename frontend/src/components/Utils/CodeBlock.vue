<template>
  <div
    class="relative flex overflow-hidden shadow-2xl  bg-cyan-500 md:rounded-xl max-h-96"
  >
    <div class="absolute inset-0 bg-black bg-opacity-75"></div>
    <div class="relative flex flex-col w-full">
      <div class="flex items-center flex-none px-4 h-11">
        <div class="flex space-x-1.5">
          <div class="w-3 h-3 border-2 border-red-500 rounded-full"></div>
          <div class="w-3 h-3 border-2 rounded-full border-amber-400"></div>
          <div class="w-3 h-3 border-2 border-green-400 rounded-full"></div>
        </div>
      </div>
      <div
        class="relative flex flex-col flex-auto min-h-0 border-t border-white  border-opacity-10"
      >
        <div
          class="absolute inset-y-0 left-0 hidden bg-black bg-opacity-25  md:block"
          style="width: 50px"
        ></div>
        <div class="flex flex-auto w-full min-h-0 overflow-auto">
          <div class="relative flex-auto w-full">
            <pre
              class="flex min-h-full text-xs md:text-sm language-javascript"
            ><div aria-hidden="true" class="flex-none hidden py-4 pr-4 text-right text-white text-opacity-50 select-none md:block" style="width:50px" id="codeblock"></div><code class="relative flex-auto block px-4 pt-4 pb-4 overflow-auto text-white"></code></pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { highlightAll } from "prismjs";
import { defineComponent, watchEffect } from "vue";

export default defineComponent({
  props: {
    code: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    watchEffect(() => {
      let lineNumber = 1;
      if (props.code) {
        for (const item in [...props.code.match(/\n/g), "\n"]) {
          const span = document.createElement("span");
          span.innerHTML = lineNumber;
          const br = document.createElement("br");
          document.getElementById("codeblock").appendChild(span);
          document.getElementById("codeblock").appendChild(br);
          lineNumber++;
        }
        const div = document.createElement("div");
        div.innerHTML = props.code;
        document.getElementsByTagName("code")[0].appendChild(div);
        highlightAll();
      }
    });
  },
});
</script>
