import sys

fo_path = "test_log.html"

# USAGE: build_html.py <log directory> <output file>

if len(sys.argv) > 2:
	out_dir = sys.argv[2]
	if out_dir[-1] == "/":
		fo_path = out_dir + fo_path
	else
		fo_path = out_dir

log_dir = sys.argv[1]

# TODO
# Read all files from log_dir
# Read SUCCESS and DATETIME
# Write HTML surroundings (Head, body, list)
# Write list item for every file
# Write SUCCESS and DATETIME
# Write log file contents
# Set color of list item depending on SUCCESS





#fo = open(fo_path, "w+")

#for line in sys.stdin:
#	sys.stdout.write(line)
#	if line[0] == '/':
#		appending = True
#	if appending:
#		out_lines.append(line)
#	print(line.split(" "))
#	if len(line.split(" ")) > 5 and line.split(" ")[5] == "FAILED:":
#		success = False


#fo.write("DATETIME="+str(datetime.datetime.now())+"\n")
#fo.write("SUCCESS="+str(success)+"\n")

#fo.writelines(out_lines)

#fo.close()
