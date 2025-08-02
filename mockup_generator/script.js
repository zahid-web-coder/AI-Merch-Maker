function displayMockup() {
  const canvas = document.getElementById("mockupCanvas");
  const ctx = canvas.getContext("2d");

  // Load the pre-rendered flux_image.png (T-shirt with design)
  const finalMockup = new Image();
  finalMockup.crossOrigin = "anonymous";
  finalMockup.src = "../content_generator/flux_image.png";  // Adjust path as needed

  finalMockup.onload = () => {
    // Fit image to canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(finalMockup, 0, 0, canvas.width, canvas.height);

    // Optional: Show JSON mockup info
    const mockupData = {
      image_used: finalMockup.src,
      description: "AI-generated design printed on T-shirt using FLUX.1 model",
      source: "Hugging Face Inference API"
    };

    document.getElementById("jsonOutput").innerText = JSON.stringify(mockupData, null, 2);
  };

  finalMockup.onerror = () => {
    alert("⚠️ Failed to load flux_image mockup.");
  };
}
