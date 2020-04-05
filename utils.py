from jinja2 import Template
import glob
import os




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















