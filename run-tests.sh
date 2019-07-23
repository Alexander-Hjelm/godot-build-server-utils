#!/bin/bash

######### BEGIN CONF #########

# Alias to the Godot executable. Must be a server build.
godot='/home/pi/godot/bin/godot_server.x11.opt.tools.32.llvm'

# Path to the Build Server Utils folder. Where this repo is installed.
PATH_TO_BUILD_UTILS="/home/pi/godot-build-server-utils"

# Path to the Godot project containing the tests.
# NOTE: This directory must contain a project.godot file and an addons/gut/ directory
PATH_TO_GODOT_PROJECT="/home/pi/godot_311_hook_test"

# Name of the logs directory. Must reside inside the Build Server Utils directory
LOG_DIR_NAME="logs"

# The html file that will be built, containing all previous test result logs
# NOTE: Make sure that the user has sufficient write permission
PATH_TO_HTML_OUTPUT="/var/www/html/godot_test_log.html"

########## END CONF ##########

### Assertions

# Assert that the project folder contains project.godot
if ! [ -e $PATH_TO_GODOT_PROJECT/project.godot ]
then
    echo "ERROR: The specified godot project path does not contain a project.godot file"
    exit 1
fi

# Assert that the project folder contains addons/gut
if ! [ -d $PATH_TO_GODOT_PROJECT/addons/gut ]
then
    echo "ERROR: The specified godot project path does not contain a addons/gut directory"
    exit 1
fi

$godot -d -s --path $PATH_TO_GODOT_PROJECT addons/gut/gut_cmdln.gd -gdir=res://test/unit -glog=0 -gexit | python3 $PATH_TO_BUILD_UTILS/parse-gut-logs.py $PATH_TO_BUILD_UTILS/$LOG_DIR_NAME;
python3 $PATH_TO_BUILD_UTILS/build-html.py $PATH_TO_BUILD_UTILS/$LOG_DIR_NAME $PATH_TO_HTML_OUTPUT;
echo "Copied log file to web server"
exit 0
