from bottle import route, run, template, static_file
import modules.content as content

@route("/<path:path>" )
def return_page(path):

    #Check if it is a static file
    dirs = path.split("/")
    if (dirs[0] == "static"):
        return static_file(path, root="")

    if (dirs[len(dirs)-2] == "media"):
        print(path)
        return static_file(path, root="", mimetype='image/jpg')


    page_content = content.get_content(f"content/{path}")
    navbar_links = content.get_dirs(f"content/{path}")
    #Check if it is home page
    if (path == "home"):
        tree_links = content.get_deep_ls(f"content/{path}")
        return template("home_page", baselink=f"/{path}", links=navbar_links, content=page_content, tree=tree_links)


    return template("basic_page", baselink=f"/{path}", links=navbar_links, content=page_content)


run(debug=True, reloader=True, port=8000)
