
# PiRover

A simple raspberry-pi driven rover that is controlled via keyboard and wifi.
In this project I used a raspberry pi 3B, 4 servo motors, and a micro breadboard.


## Installation

PIGPIOD is required to run this project.

```bash
 wget https://github.com/joan2937/pigpio/archive/master.zip
 unzip master.zip
 cd pigpio-master
 make
 sudo make install
```

Then simply run the python file named "servo.py", and enjoy!
Use the WSAD keys to control the rover, and the E key to stop all motors at once.




    
## Diagrams

![alt text](https://github.com/WeasalCrafter/PiRover/blob/main/diagram.png?raw=true)
![alt text](https://github.com/WeasalCrafter/PiRover/blob/main/pinout.png?raw=true)

## Acknowledgements

- [More information about the pigpiod library](http://abyz.me.uk/rpi/pigpio/download.html )


## Authors

- [Logan Fick](https://www.github.com/weasalcrafter)

