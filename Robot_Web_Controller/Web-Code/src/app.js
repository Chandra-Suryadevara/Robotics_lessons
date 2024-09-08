const http = require('http');
const fs = require('fs');
const path = require('path');
const { SerialPort } = require('serialport');
const express = require('express');
const socketIo = require('socket.io');

// Express app setup
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, '../public')));

// Serve the index.html file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

// Serial port setup
const port = new SerialPort({
  path: '/dev/ttyACM0',
  baudRate: 9600,
  dataBits: 8,
  parity: 'none',
  stopBits: 1,
  flowControl: false,
});

// Socket.io connection
io.on('connection', (socket) => {
  console.log('Node is listening to port');

  // Handle data received from the WebSocket
  socket.on('data', (data) => {
    console.log('Received data from WebSocket:', data);

    // Ensure data is a Buffer and has 12 bytes
    if (Buffer.isBuffer(data) && data.length === 12) {
      // Send the 12-byte data to the serial port
      port.write(data, (err) => {
        if (err) {
          console.error('Error writing to serial port:', err.message);
        } else {
          console.log('Data sent to serial port successfully');
        }
      });
    } else {
      console.error('Received data is not a 12-byte Buffer');
    }
  });
});

// Start the server
server.listen(3000, () => {
  console.log('Server is running on port 3000');
});




/*

var SerialPort = require("serialport");


var port = new SerialPort('/dev/ttyACM0',{ baudRate: 9600,
  dataBits: 8,
  parity: 'none',
  stopBits: 1,
  flowControl: false
});

const express = require('express');
const path = require('path');
const app = express();
const port = 3000

// Serve static files from the current directory
app.use(express.static(path.join(__dirname, '../public')));

// Serve the index.html file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(port, (error) => {
  if (error) {
    console.log('Something Went Wrong', error);
  } else {
    console.log('Server is listening on port ' + port);
  }
});
*/