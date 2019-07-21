import os
import sys

fo_path = "test_log.html"

# USAGE: build_html.py <log directory> <output file>
if len(sys.argv) <= 2:
	print("USAGE: build_html.py <log directory> <output file>")
	sys.exit(1)

log_dir = sys.argv[1]
out_dir = sys.argv[2]

if out_dir[-1] == "/":
	fo_path = out_dir + fo_path
else:
	fo_path = out_dir

# Write surrounding HTML
html_out_file = open(fo_path, "w+")
html_out_file.write("<html>\n<head>\n<title>Godot build results</title>\n</head>\n<body>\n")

for root, dirs, files in os.walk(log_dir, topdown=True):
	for name in sorted(files, reverse=True):
		full_name = os.path.join(root, name)
		log_file = open(full_name, "r+")

		content = log_file.readlines()
		reading_meta = True
		meta_success = ""
		meta_datetime = ""
		wrote_div_top = False

		# Write HTML list item for this log
		html_out_file.write("<div ")

		for x in range(0, len(content)):
			line = content[x]
			if reading_meta:
				meta_line = line.split("=")
				if(len(meta_line) > 1):
					if meta_line[0] == "SUCCESS":
						meta_success = meta_line[1].rstrip()
					elif meta_line[0] == "DATETIME":
						meta_datetime = meta_line[1].rstrip()
				else:
					reading_meta = False

			else:
				if not wrote_div_top:
					wrote_div_top = True

					html_out_file.write(" style=\"background-color: ")
					if meta_success == "True":
						html_out_file.write("#b3ffb3")
					else:
						html_out_file.write("#ffb3b3");

					html_out_file.write("\">\n<h2>\n" + meta_datetime + "\n")

					if meta_success == "True":
						html_out_file.write("BUILD SUCCEEDED\n")
					else:
						html_out_file.write("BUILD FAILED\n")

					html_out_file.write("</h3>\n<br />\n")
				html_out_file.write(line + "<br />")

		html_out_file.write("</div>\n")
		log_file.close()

# Write trailing HTML
html_out_file.write("</body>\n</html>\n")
html_out_file.close()

print("Created test report html file")
