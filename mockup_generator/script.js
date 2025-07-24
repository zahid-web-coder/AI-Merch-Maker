function generateMockup() {
  const canvas = document.getElementById("mockupCanvas");
  const ctx = canvas.getContext("2d");

  // Clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Load base T-shirt template
  const tshirtImg = new Image();
  tshirtImg.crossOrigin = "anonymous";
  tshirtImg.src = "https://i.ibb.co/8nW09dDw/t-shirt.png"; // T-shirt base image

  tshirtImg.onload = () => {
    ctx.drawImage(tshirtImg, 0, 0, canvas.width, canvas.height);

    // Load user design image to overlay
    const userImg = new Image();
    userImg.crossOrigin = "anonymous";
    userImg.src = "https://i.ibb.co/kVQGMB4P/waterfall.jpg"; // ✅ Your uploaded waterfall image

    userImg.onload = () => {
      // Draw design onto t-shirt
      ctx.drawImage(userImg, 150, 200, 290, 290); // Adjust placement here

      // Generate mockup JSON
      const mockupData = {
        product: "T-shirt",
        placement: "front",
        print_area: "300x300 px",
        mockup_image: canvas.toDataURL("image/png"),
        image_source: userImg.src
      };

      document.getElementById("jsonOutput").innerText = JSON.stringify(mockupData, null, 2);
    };

    userImg.onerror = () => {
      alert("Failed to load user design image.");
    };
  };

  tshirtImg.onerror = () => {
    alert("Failed to load t-shirt base image.");
  };
}
