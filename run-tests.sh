#!/bin/bash
/home/pi/godot/bin/godot_server.x11.opt.tools.32.llvm -d -s --path /home/pi/godot_311_hook_test/ addons/gut/gut_cmdln.gd -gtest=res://test/unit/test_example.gd -glog=0 -gexit | python3 /home/pi/godot-build-server-utils/parse-gut-logs.py /home/pi/godot-build-server-utils/logs;
python3 /home/pi/godot-build-server-utils/build-html.py /home/pi/godot-build-server-utils/logs /var/www/html/godot_test_log.html;
echo "Copied log file to web server"
