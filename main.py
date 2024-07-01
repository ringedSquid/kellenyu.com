from bottle import route, run, template, static_file
import modules.content as content

@route("/<path:path>" )
def return_page(path):

    #Check if it is a static file
    dirs = path.split("/")
    if (dirs[0] == "static"):
        print("STATIC", path)
        return static_file(path, root="")

    #Check if it is home page
    if (dirs[0] == "home"):
        print(content.get_deep_ls(f"content/{path}"))


    page_content = content.get_content(f"content/{path}")
    navbar_links = content.get_dirs(f"content/{path}")
    return template("basic_page", baselink=f"/{path}", links=navbar_links, content=page_content)


run(debug=True, reloader=True, port=8000)
