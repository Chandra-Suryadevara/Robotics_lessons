var socket = io();

class MotorController {
  constructor() {}

  stopAllMotors() {
    // Define a 12-byte array with default values
    const byteArray = new Uint8Array([1, 1, 0, 2, 1, 0, 3, 1, 0, 4, 1, 0]);
    this.sendData(byteArray);
  }
  
  sendData(data) {
    socket.emit('data', data); // Emitting the data to the server
  }
  
  goLeft(speed) {
    const byteArray = new Uint8Array([1, 1, speed, 2, 0, speed, 3, 1, speed, 4, 0, speed]);
    this.sendData(byteArray);
  }

  goRight(speed){
    const byteArray = new Uint8Array([1, 0, speed, 2, 1, speed, 3, 0, speed, 4, 1, speed]);
    this.sendData(byteArray);
  }

  goForward(speed) {
    const byteArray = new Uint8Array([1, 1, speed, 2, 1, speed, 3, 1, speed, 4, 1, speed]);
    this.sendData(byteArray);
  }

  goBackward(speed) {
    const byteArray = new Uint8Array([1, 0, speed, 2, 0, speed, 3, 0, speed, 4, 0, speed]);
    this.sendData(byteArray);
  }


}

const controller = new MotorController();

let set_speed = 0;

document.getElementById("frontBtn").addEventListener("click", function () {
  console.log("Front button pressed");
  controller.goForward(set_speed);
});

document.getElementById("backBtn").addEventListener("click", function() {
  console.log("Back button pressed");
  controller.goBackward(set_speed);
});

document.getElementById("leftBtn").addEventListener("click", function() {
    console.log("Left button pressed");
    controller.goLeft(set_speed);
});

document.getElementById("rightBtn").addEventListener("click", function() {
  console.log("Right button pressed");
  controller.goRight(set_speed);
});

document.getElementById("brakeBtn").addEventListener("click", function() {
    console.log("Brake button pressed");
    controller.stopAllMotors();
});

document.getElementById("KillSwitch").addEventListener("change", function() {
    if (this.checked) {
        console.log("Brake ON");
    } else {
        console.log("Brake OFF");
    }
});

document.getElementById("speed").addEventListener("input", function() {
    console.log("speed: " + this.value);
    set_speed = this.value // Ensure speed is an integer
});
