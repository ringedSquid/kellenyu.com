# Robot Tour
Multiple robots capable of traversing through an obstacle course with millimeter precision.
## Clinton
Simple differential drive
<img src="./Robot-Tour/media/Clinton_CAD.png" alt="Clinton_CAD" width="75%">

* ESP32 MCU, DRV8874 Motor Driver
* Pure Pursuit implementation

<br>
## Robert
Simple stepper motor design, first custom PCB & machined chassis
<img src="./Robot-Tour/media/Robert_CAD.png" alt="Robert_CAD" width="75%">

* ESP32 MCU, BMI270 IMU, TMC2209 & A4988 Motor Driver
* SD Card input for path programming, OLED Display

<br>
## Beter
More complex stepper motor design
<img src="./Robot-Tour/media/Beter_CAD_OLD.png" alt="Beter_CAD_OLD" width="75%">
<img src="./Robot-Tour/media/Beter_CAD.png" alt="Beter_CAD" width="75%">

* ESP32 MCU, TMC2209 Motor Driver, BMI270 IMU
* Quadature Encoder + OLED for user interface
* All-in-one PCB board
    * Same board used on two different chassis
* Dual IMU integration
