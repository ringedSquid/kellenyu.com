# Cost Effectvie Soil Moisture Sensor
My 1st place entry for the 2024 IEEE SSCS Arduino Contest
### [github repo](https://github.com/ringedSquid/Cost_Effective_Soil_Moisture_Sensor_SSCS-2024/tree/main) [youtube video](https://www.youtube.com/watch?v=Hh_UeHd2Llg)
<br>

## Reducing water usage in agriculture
The goal of this project was to improve current agricultural watering methods. Farmers typically water their crops using according to a set schedule, however crops do not use up water in a uniform manner and do it at different rates according to the time of year. Apart from cost, processing freshwater also has a large carbon footprint. If farmers are able to monitor the water levels within their field, then they can selectively water crops and lower their overall water usage.
<br>

## Low cost
Lowering the cost of these soil sensors is very important because if any technology is to have an impact on the world, it must be accessible to the masses. I used a cheap microcontroller (ATtiny414), and utilized a LED+Computer Vision system to transmit data about the soil (as opposed to an expensive and power hungry radio setup). I planned to have a drone or any device with a camera be able to read the LEDs on the sensor (first a light needs to be directed on them to wake them up from sleep) and create a moisture map of the entire field.
<br>

## How to measure moisture?
Soil can act as a dielectric in a capacitor. When the moisture of the soil changes, so does the dielectric properties of the soil. I created a capacitor directly on my PCB in the form of large parallel traces and used a simple RC circuit setup to measure the capacitance. Different capacitances correspond to different soil moisture levels.