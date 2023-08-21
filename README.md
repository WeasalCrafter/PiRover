
# PiRover

A raspberry pi powered rover controlled using a web interface hosted on a localhost Flask server. You'll need to setup the raspberry pi as a wireless access point, follow this tutorial: https://www.tomshardware.com/how-to/raspberry-pi-access-point

## Installation and Usage

Install the Pigpio Daemon

```bash
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
```
Install Flask

```bash
sudo apt-get install python3-flask
```

Download and unzip this project
```bash
wget https://github.com/WeasalCrafter/PiRover/archive/refs/heads/main.zip
sudo unzip main.zip
cd main
```

You'll need your raspberry pi's ipv4 address in order to view the web panel
```bash
ifconfig
```

Run the program!
```bash
sudo python main.py
```
You can access the webpanel on any browser connected to the same network as the PiRover at "http://x.x.x.x:5000" where "x.x.x.x" represents the ipv4
    
## Acknowledgements

 - [Pigpio Library](http://abyz.me.uk/rpi/pigpio/)
 - [Flask Library](https://flask.palletsprojects.com)

