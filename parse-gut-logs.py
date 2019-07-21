import datetime
import sys

print("Running GUT test suite...")

appending = False

fo_name = "test_output_" + str(datetime.datetime.now()).replace(" ", "_")

if len(sys.argv) <= 1:
	print("USAGE: python3 parse-gut-logs.py <log output directory>")
	sys.exit(1)

out_dir = sys.argv[1]
if not out_dir[-1] == "/":
	out_dir += "/"

fo_name = out_dir + fo_name
fo = open(fo_name, "w+")

out_lines = []

success = True


for line in sys.stdin:
	if line[0] == '/':
		appending = True
	if appending:
		out_lines.append(line)
	if len(line.split(" ")) > 5 and line.split(" ")[5] == "FAILED:":
		success = False


fo.write("DATETIME="+str(datetime.datetime.now())+"\n")
fo.write("SUCCESS="+str(success)+"\n")

fo.writelines(out_lines)

fo.close()

if success:
	print("All GUT tests ran SUCCESSFULLY. :)")
else:
	print("GUT test suite FAILED! Please check https://www.groove.cool/godot_test_log.html for the test report.")
