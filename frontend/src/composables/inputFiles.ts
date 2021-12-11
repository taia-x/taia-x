import { ref } from "vue";

/**
 * composable for managing input files
 */
const inputFiles = () => {
  const files: any = ref([]);
  const image = ref("");
  const data = ref("");

  const dataReader = new FileReader();
  const imageReader = new FileReader();

  dataReader.onload = (e: any) => {
    data.value = JSON.parse(e.target.result);
  };

  imageReader.onload = (e: any) => {
    image.value = e.target.result;
  };

  /**
   * reads input file as text or image, depending on data type
   * @param e input file event
   */
  const onFileSelected = (e: any): void => {
    files.value =
      Array.from(e.target?.files) || Array.from(e.dataTransfer?.files);
    files.value.forEach((file: File) => {
      const fileExtension: string = file.name.substr(file.name.indexOf("."));
      if (file.type === "application/json" && fileExtension === ".json") {
        dataReader.readAsText(file);
      }
      if (file.type === "image/png" && fileExtension === ".png") {
        imageReader.readAsArrayBuffer(file);
      }
    });
  };

  const removeFile = (index: number) => {
    files.value.splice(index, 1);
  };

  return { files, image, data, onFileSelected, removeFile };
};

export default inputFiles;
