import utils
import sys
print("This is argv:", sys.argv)



command = sys.argv[1]
print(command)
if command == "build":
	print("Build was specified")
	utils.generate_pages()
elif command == "new":
	print("New page was specified")
	utils.new_page()
else:
	print("Please specify ’build’ or ’new’")