from flask import Flask, render_template, request, escape, session
import os

app = Flask(__name__)
app.secret_key = "Kommernetkrumm"


@app.route('/')
def entry_page() -> 'html':
    myhost = os.uname()
    return render_template ("base.html", the_host=myhost[1], the_sysname=myhost[0], the_version=myhost[3],
     the_title="Demo Web App")



if __name__ == '__main__':
    app.run(debug=True)