Here is a manual way to install Sopcast for Ubuntu (14.04):
Download sp-auth.tgz and libstdcpp5.tgz to /tmp from http://www.sopcast.com/download/linux.html .

Download sopcast-player-0.8.5.tar.gz to /tmp from https://code.google.com/p/sopcast-player/downloads/list 

Install the missing libs:
$ cd /tmp
$ tar -zxvf libstdcpp5.tgz
$ sudo mv /tmp/usr/bin/libstdc++.so.5.0.1 /usr/bin/
$ sudo ln -s /usr/bin/libstdc++.so.5.0.1 /usr/bin/libstdc++.so.5
$ rm -rf /tmp/usr

Install the sopcast backend:
$ tar -zxvf sp-auth.tgz
$ sudo mv /tmp/sp-auth/sp-sc-auth /usr/bin/
$ sudo rm -rf /tmp/sp-auth

Install the sopcast frontend:
$ sudo apt-get install vlc python gettext python-setuptools
$ sudo apt-get install libvlc-dev hicolor-icon-theme python-glade2 python-gobject python-gtk2
$ tar -zxvf sopcast-player-0.8.5.tar.gz
$ cd sopcast-player
$ make
$ sudo make install
$ cd ~; rm -rf /tmp/sopcast-player

Open the Firefox and type about:config
Create a new string with name network.protocol-handler.app.sop and value sopcast-player

Now try to open sop:// link and you will be presented with dialog box where you can search location of sopcast player. Navigate to /usr/bin/sopcast-player and click OK.
