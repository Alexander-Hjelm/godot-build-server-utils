~/godot/bin/godot_server.x11.opt.tools.32.llvm -d -s --path ~/godot_311_hook_test/ addons/gut/gut_cmdln.gd -gtest=res://test/unit/test_example.gd -glog=0 -gexit | python3 ~/godot-build-server-utils/parse-gut-logs.py ~/godot-build-server-utils/logs;
python3 ~/godot-build-server-utils/build-html.py ~/godot-build-server-utils/logs
