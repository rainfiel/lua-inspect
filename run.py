

import os
import shutil

top = "/Users/rainfiel/Desktop/Work/dapili/trunk/tech/rawres/script"
top_folders = top.split("/")

def inspect(lua, html, htmllib):
	cmd = "./luainspect -fhtml -l%s %s > %s" % (htmllib, lua, html)
	os.system(cmd)

parsed_root = set()
def processFile(root, filename):
	if not filename.endswith(".lua"):
		return
	if root.endswith("PL/data"):
		return

	folders = root.split("/")
	if root not in parsed_root:
		parsed_root.add(root)
		output_dir = "output"
		for i in xrange(len(top_folders), len(folders)):
			output_dir = "%s/%s"%(output_dir, folders[i])
			if not os.path.exists(output_dir):
				os.mkdir(output_dir)

	lua = "%s/%s"%(root, filename)
	html = "/".join(folders[len(top_folders):])
	htmllib = "../"*(len(folders)-len(top_folders)+1) + "htmllib"
	if html:
		html = "output/%s/%s.html" % (html, filename[:-4])
	else:
		html = "output/%s.html" % filename[:-4]
	inspect(lua, html, htmllib)

def walk():
	for root, dirs, files in os.walk(top):
	    for i in files:
	    	processFile(root, i)

def prepare():
	if os.path.exists("output"):
		shutil.rmtree("output")
	os.mkdir("output")

if __name__ == "__main__":
	prepare()
	walk()
