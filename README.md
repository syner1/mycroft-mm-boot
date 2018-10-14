## Magic Mirror Mycroft Skill
A simple skill to shutdown/restart/start Magic Mirror by voice.

## Description
This skill allows the user to turn off, start, restart Magic Mirror (tested on Rpi) gracefully, with a voice confirmation (yes).

## Requires
	sudo npm install -g pm2
	pm2 startup //PM2 will now show you a command you need to execute.

## Make a MagicMirror start script.
	To use PM2 in combination with MagicMirror, we need to make a simple shell script. Preferable, we put this script outside the MagicMirror folder to make sure it won't give us any issues if we want to upgrade the mirror.

	cd ~
	nano mm.sh
	Add the following lines:

	cd ~/MagicMirror
	DISPLAY=:0 npm start
	Save and close, using the commands CTRL-O and CTRL-X. 
	
	Now make sure the shell script is executable by performing the following command:
	chmod +x mm.sh
	
	Test:
		in these steps:
			pm2 start mm.sh // to start magic mirror (wait a bit till it loads)
			pm2 stop mm // to stop magic mirror
			pm2 save // save current state (make sure magic mirror is stopped
	
## Examples
	magic mirror shutdown
	magic mirror poweroff
	magic mirror die
	magic mirror off
	magic mirror disable

	magic mirror reboot
	magic mirror restart

	magic mirror start
	magic mirror on
	magic mirror boot
	magic mirror enable



