# This code is designed to run on an ESP32 board using the Arduino IDE.
# Use python for this


#include <WiFi.h>
#include <WebServer.h>
#include <ESPmDNS.h>
#include <ArduinoJson.h>
#include <Servo.h>
const char* ssid = "your_SSID";  // Replace with your WiFi SSID
const char* password = "your_PASSWORD";  // Replace with your WiFi password
WebServer server(80);
Servo doorServo;  // Create a Servo object to control the door lock
const int servoPin = 5;  // Pin connected to the servo motor
void setup() {
    Serial.begin(115200);
    doorServo.attach(servoPin);  // Attach the servo to the specified pin
    WiFi.begin(ssid, password);
    
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    
    Serial.println("Connected to WiFi");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
    
    server.on("/", handleRoot);
    server.on("/unlock", handleUnlock);
    server.on("/lock", handleLock);
    
    server.begin();
    Serial.println("HTTP server started");
}
void loop() {
    server.handleClient();
}
void handleRoot() {
    String html = "<html><body>";
    html += "<h1>Smart Door Lock System</h1>";
    html += "<button onclick=\"location.href='/unlock'\">Unlock Door</button>";
    html += "<button onclick=\"location.href='/lock'\">Lock Door</button>";
    html += "</body></html>";
    server.send(200, "text/html", html);
}
void handleUnlock() {
    doorServo.write(90);  // Adjust the angle to unlock the door
    server.send(200, "text/plain", "Door Unlocked");
    Serial.println("Door Unlocked");
}
void handleLock() {
    doorServo.write(0);  // Adjust the angle to lock the door
    server.send(200, "text/plain", "Door Locked");
    Serial.println("Door Locked");
}
