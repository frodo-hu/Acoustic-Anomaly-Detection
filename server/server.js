const mqtt = require('mqtt');
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 4000;

// Use your AWS EC2 public IP address
const mqttClient = mqtt.connect('mqtt://13.60.185.105:1883');  // Replace with your AWS EC2 public IP

let piData = {}; // This will hold the latest data from Raspberry Pis

mqttClient.on('connect', () => {
    console.log('Connected to AWS MQTT broker');
    // Subscribe to the 'pi-data' topic where Raspberry Pis send their data
    mqttClient.subscribe('pi-data', (err) => {
        if (!err) {
            console.log('Subscribed to pi-data topic');
        }
    });
});

mqttClient.on('message', (topic, message) => {
    if (topic === 'pi-data') {
        const data = JSON.parse(message.toString());
        console.log('Data received from Raspberry Pi:', data);
        piData = data;  // Store the latest data received from Raspberry Pis
    }
});

// Route to fetch the latest data from Raspberry Pis
app.get('/latest-data', (req, res) => {
    res.json(piData);
});

// Start the Express server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});