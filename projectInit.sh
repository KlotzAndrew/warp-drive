#! /bin/bash

sudo cp warp-drive /etc/init.d
sudo update-rc.d warp-drive defaults 98

# sudo update-rc.d -f warp-drive remove

