<?php
// Allow CORS for testing
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

// 📥 Receive incoming JSON
$data = json_decode(file_get_contents("php://input"), true);

// 📁 Save to file (optional)
file_put_contents("published_product.json", json_encode($data, JSON_PRETTY_PRINT));

// 🔁 Respond
echo json_encode([
  "status" => "received",
  "product_title" => $data["title"] ?? "N/A",
  "image_used" => $data["image_source"] ?? "none",
  "tags" => $data["auto_tags"] ?? []
]);
?>
