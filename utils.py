from jinja2 import Template
import glob
import os


# print("Building Static Sites")


pages = []

def generate_list():
	content_files= glob.glob("content/*.html")

	for file_path in content_files:
		file_name = os.path.basename(file_path)
		name_only, extension = os.path.splitext(file_name)
		title_only = name_only
		output_path = 'docs/' + file_name
		

		pages.append({
			"file_name": file_name,
			"title": title_only,
			"output": output_path})





# loop
def generate_pages():
	generate_list()

	template_contents=open('templates/base.html').read()
	apply_template = Template(template_contents)

	for page in pages:
		file_path = 'content/' + page['file_name']
		content = open(file_path).read()
		full_page = apply_template.render(
			title= page['title'],
			main_content = content, 
			page_list = pages)
		open(page['output'], 'w+').write(full_page)
	
	return full_page

def new_page():
	open('content/new_content_page.html', 'w+').write("""<h1>New Content!</h1> 

		<p>New Content...</p>""")















# for page in pages:
	# 	file_name = page["file_name"]
	# 	output = page["output"]
	# 	title = page["title"]
	# 	content = open(file_name).read()
	# 	full_page = apply_template(content, title)
	# 	final_output = produce_output(output, full_page)
		



# #templating
# def apply_template(content, title):
# 	template = open("templates/base.html").read()
# 	template_with_content = template.replace("{{content}}", content)
# 	full_page = template_with_content.replace("{{title}}", title)
# 	return full_page


# #produce output
# def produce_output(output, full_page):
# 	open(output, 'w+').write(full_page)

# if __name__ == "__main__":
# 	main()



#previous code for reference.

# print('building static site')
# 	top_html = open('templates/top.html').read()
# 	bottom_html = open('templates/bottom.html').read()

# 	#index
# 	middle_html = open('content/index.html').read()
# 	combined_html = top_html + middle_html + bottom_html
# 	open('docs/index.html', 'w+').write(combined_html)

# 	#projects
# 	print('building static site')
# 	middle_html = open('content/projects.html').read()
# 	combined_html = top_html + middle_html + bottom_html
# 	open('docs/projects.html', 'w+').write(combined_html)

# 	#contact
# 	print('building static site')
# 	middle_html = open('content/contact.html').read()
# 	combined_html = top_html + middle_html + bottom_html
# 	open('docs/contact.html', 'w+').write(combined_html)
