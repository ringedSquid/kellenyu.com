from bottle import route, run, template, static_file
import modules.content as content

@route("/<filename>" )
def index(filename):
    page_content = content.get_content(f"content/{filename}")
    navbar_links = content.get_dirs(f"content/{filename}")
    return template("basic_page", baselink=f"/{filename}", links=navbar_links, content=page_content)

@route("/static/<filename>")
def static(filename):
    return static_file(filename, root="static/")

run(debug=True, reloader=True, port=8000)
