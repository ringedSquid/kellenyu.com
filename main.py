from bottle import route, run, template, static_file
import modules.content as content

@route("/<path:path>" )
def return_page(path):
    dirs = path.split("/")
    if (dirs[0] == "static"):
        print("STATIC", path)
        return static_file(path, root="")

    page_content = content.get_content(f"content/{path}")
    navbar_links = content.get_dirs(f"content/{path}")
    return template("basic_page", baselink=f"/{path}", links=navbar_links, content=page_content)


run(debug=True, reloader=True, port=8000)
