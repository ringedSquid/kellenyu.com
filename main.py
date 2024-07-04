from bottle import route, run, template, static_file, redirect
import modules.content as content
import os

@route("/")
def root_page():
    redirect("/home")

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
    if (content.is_tree(f"content/{path}")):
        tree_links = content.get_deep_ls(f"content/{path}")
        return template("tree_page", baselink=f"/{path}", links=navbar_links, content=page_content, tree=tree_links)


    return template("basic_page", baselink=f"/{path}", links=navbar_links, content=page_content)

if __name__ == "__main__":
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, debug=True)
