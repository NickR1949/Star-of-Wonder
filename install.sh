sudo mkdir /media/usb
sudo chown -R pi:pi /media/usb
sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi
cp -r /media/usb/Star .
curl https://get.pimoroni.com/blinkt | bash
cp /media/usb/launcher.sh .
chmod 755 launcher.sh
mkdir logs
sudo unmount /media/usb
sudo crontab -e


