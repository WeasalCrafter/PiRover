 ___  ___  ___   ___  __   __ ___  ___ 
| _ \|_ _|| _ \ / _ \ \ \ / /| __|| _ \
|  _/ | | |   /| (_) | \   / | _| |   /
|_|  |___||_|_\ \___/   \_/  |___||_|_\

INSTALLING PIGPIOD:
 - wget https://github.com/joan2937/pigpio/archive/master.zip
 - unzip master.zip
 - cd pigpio-master
 - make
 - sudo make install

To start the pigpio daemon:
 - sudo pigpiod
To stop the pigpio daemon:
 - sudo killall pigpiod

Then simply run the python file named "servo.py", and enjoy!
