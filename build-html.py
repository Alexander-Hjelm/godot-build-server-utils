import os
import sys

fo_path = "test_log.html"

# USAGE: build_html.py <log directory> <output file>

if len(sys.argv) > 2:
	out_dir = sys.argv[2]
	if out_dir[-1] == "/":
		fo_path = out_dir + fo_path
	else:
		fo_path = out_dir

log_dir = sys.argv[1]

# Write surrounding HTML
html_out_file = open(fo_path, "w+")
html_out_file.write("<html>\n<head>\n<title>Godot build results</title>\n</head>\n<body>\n")

for root, dirs, files in os.walk(log_dir, topdown=True):
	for name in files:
		full_name = os.path.join(root, name)
		log_file = open(full_name, "r+")

		print("Read log file: " + full_name)
		content = log_file.readlines()
		reading_meta = True
		meta_success = ""
		meta_datetime = ""
		wrote_first_content_line = False

		# Write HTML list item for this log
		html_out_file.write("<div>\n<h3>\n")

		for x in range(0, len(content)):
			line = content[x]
			if reading_meta:
				meta_line = line.split("=")
				if(len(meta_line) > 1):
					if meta_line[0] == "SUCCESS":
						meta_success = meta_line[1].rstrip()
						if meta_success:
							html_out_file.write("BUILD SUCCEEDED\n")
						else:
							html_out_file.write("BUILD FAILED\n")
					elif meta_line[0] == "DATETIME":
						meta_datetime = meta_line[1].rstrip()
						html_out_file.write(meta_datetime + "\n")
				else:
					reading_meta = False
			else:
				if not wrote_first_content_line:
					html_out_file.write("</h3>\n<br />\n")
					wrote_first_content_line = True
				html_out_file.write(line + "<br />")
		html_out_file.write("</div>\n")
		log_file.close()

# Write trailing HTML
html_out_file.write("</body>\n</html>\n")
html_out_file.close()

# TODO
# Set color of list item depending on SUCCESS
