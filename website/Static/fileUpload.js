// fileUpload.js

document.getElementById("file").addEventListener("change", handleFileUpload);

function handleFileUpload() {
  const fileInput = document.getElementById("file");
  const file = fileInput.files[0];

  if (file && file.name.endsWith(".docx")) {
    const formData = new FormData();
    formData.append("file", file);

    // Send the file to the server for processing
    axios.post("/upload", formData, {
      headers: { "Content-Type": "multipart/form-data" },
      responseType: "blob", // Expect a binary response
    })
      .then((response) => {
        // Create a download link for the processed file
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const a = document.createElement("a");
        a.href = url;
        a.download = "foci_file.txt";
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
      })
      .catch((error) => {
        console.error("Error uploading file:", error);
      });
  } else {
    alert("Please select a valid .docx file.");
  }
}
