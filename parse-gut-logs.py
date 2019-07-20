import datetime
import sys

appending = False

fo_name = "test_output_" + str(datetime.datetime.now())

if len(sys.argv) > 1:
	out_dir = sys.argv[1]
	if not out_dir[-1] == "/":
		out_dir += "/"
	fo_name = out_dir + fo_name

fo = open(fo_name, "w+")

out_lines = []

success = True


for line in sys.stdin:
	sys.stdout.write(line)
	if line[0] == '/':
		appending = True
	if appending:
		out_lines.append(line)
	print(line.split(" "))
	if len(line.split(" ")) > 5 and line.split(" ")[5] == "FAILED:":
		success = False


fo.write("DATETIME="+str(datetime.datetime.now())+"\n")
fo.write("SUCCESS="+str(success)+"\n")

fo.writelines(out_lines)

fo.close()
