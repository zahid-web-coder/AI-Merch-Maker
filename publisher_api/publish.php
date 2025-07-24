<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

// Check request method
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode([
        "status" => "error",
        "message" => "Invalid request method"
    ]);
    exit;
}

$raw = file_get_contents("php://input");
$input = json_decode($raw, true);

if ($input) {
    file_put_contents("log.txt", json_encode($input, JSON_PRETTY_PRINT));

    echo json_encode([
        "status" => "success",
        "product_id" => "mock-" . rand(1000, 9999)
    ]);
} else {
    file_put_contents("log.txt", "❌ ERROR: No input received\nRaw: $raw");

    echo json_encode([
        "status" => "error",
        "message" => "No data received"
    ]);
}
?>
