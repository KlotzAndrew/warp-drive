# Warp Drive

A physical button that starts a Jenkins job. This designed for  aRaspberry Pi, 
connected to two toggle switches and a button. Deploy an app or run a job in
style.

* Toggle switch A
* Toggle switch B
* Hit button to launch

### Setup

 * warp-drive is expected to be in the directory `/home/pi/scripts/warp-drive`
 * copy `jenkins.yml.sample` to `jenkins.yml` with your configs
 * `sudo cp warp-drive.sh /etc/init.d`
 * restart the system and it will be running (all the wires need to be setup!)

### Controls

Automatically runs when plugged in, but if you want to ssh in and manually start
or stop the script, use:

```bash
sudo /etc/init.d/warp-drive.sh start
sudo /etc/init.d/warp-drive.sh stop
sudo /etc/init.d/warp-drive.sh restart
```

