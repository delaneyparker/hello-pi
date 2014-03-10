#hello-pi#
How to get a Raspberry Pi set up for development of web applications. This doc is based on notes taken while setting up Django on a Pi. Hopefully they’ll help you get started!

##Hardware##
* Raspberry Pi - Model B [[link](http://bit.ly/ObVbln)]
* Patriot 16GB Class 10 SD card [[link](http://amzn.to/1kGOUfC)]  
* USB WiFi adapter [[link](http://amzn.to/1cp7upq)]

##Installation##
Follow instructions on raspberrypi.org for NOOBS install to SD card. [[link](http://bit.ly/1cIbjGV)]

##Configuration##
After installation, the GUI config tool raspi-config will run. Feel free to make whatever changes you like. Below are the settings I like to use. Remember if you make changes, you’ll have to reboot.

    $ cat /boot/config.txt
    # Turn off overscan, overclock a little (CPU @ 900 MHz, RAM @ 450 MHz):
    hdmi_force_hotplug=1
    config_hdmi_boost=4
    disable_overscan=1
    core_freq=250
    sdram_freq=450
    over_voltage=2

##Update system##

    $ sudo apt-get update
    $ sudo apt-get upgrade

##Optional Changes##
Here are a few other changes I like to make on my system for development. Feel free to take them or leave them, just don’t let me catch you installing Emacs. ;-)

###Change clock from UTC to PT###

    $ sudo ln -sf /usr/share/zoneinfo/US/Pacific /etc/localtime

###Setup Vim###
Skip the map command if you don’t want ; and : swapped, I’m crazy like that.

    $ sudo apt-get install vim
    $ cat ~/.vimrc
    map ; :
    set ai
    set et
    set nu
    set ru
    set sm
    set sw=2
    set ts=2
    syntax enable
    
##Python##
Already installed!

##pip##
    
    $ wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    $ sudo python get-pip.py

##virtualenv / virtualenvwrapper##

    $ sudo pip install virtualenv virtualenvwrapper
    $ echo export WORKON_HOME=~/.virtualenvs >> ~/.profile
    $ echo source /usr/local/bin/virtualenvwrapper.sh >> ~/.profile
    $ source ~/.profile

##Running the example Django application - hello-pi##
###Create virtualenv named: hello-pi###

    $ mkvirtualenv hello-pi

###Grab hello-pi source###

    $ git clone https://github.com/delaneyparker/hello-pi.git
    $ cd hello-pi
    $ pip install -r requirements.txt
    $ cd hello_project

###Now you can run the app!###

    $ python manage.py runserver 0:8000

####Visit http://localhost:8000/hello from a web browser.####
