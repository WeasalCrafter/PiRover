PIROVER

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
