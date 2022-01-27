import { ref } from "vue";
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// import { saveAs } from "file-saver";
import JSZip from "jszip";

/**
 * composable for managing input files
 */
const inputFiles = () => {
  const files: any = ref([]);
  const archive = ref(new Blob());
  const zip = new JSZip();

  const onFileSelected = async (e: any): Promise<void> => {
    const newFiles: any = e?.target?.files
      ? Array.from(e.target.files)
      : Array.from(e.dataTransfer.files);
    if (files.value.length === 0) {
      files.value = newFiles;
    } else {
      newFiles.forEach((file: File) => {
        const index = files.value.findIndex((f: File) => f.name === file.name);
        if (index > -1) {
          files.value[index] = file;
        } else {
          files.value.push(file);
        }
      });
    }
    files.value.forEach((file: File) => {
      zip.file(file.name, file);
    });
    archive.value = await zip.generateAsync({ type: "blob" });
  };

  const removeFile = async (index: number): Promise<void> => {
    const file = files.value[index];
    zip.remove(file.name);
    archive.value = await zip.generateAsync({ type: "blob" });
    files.value.splice(index, 1);
  };

  const generateSHA256 = async (archive: Blob): Promise<string> => {
    const hashBuffer = await crypto.subtle.digest(
      "SHA-256",
      await archive.arrayBuffer()
    );

    // convert ArrayBuffer to Array
    const hashArray = Array.from(new Uint8Array(hashBuffer));

    // convert bytes to hex string
    return hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
  };

  return { files, archive, generateSHA256, onFileSelected, removeFile };
};

export default inputFiles;
