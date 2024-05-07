__author__ = "Kaya Arkin"
__date__ = "21/04/2024"


from scripts.logger import Logger
from scripts.save_load_data import load_json
from flask import Flask, render_template, redirect


## Loading Logger and initialising.
Logger("logs/Webpage_Log")


## Loading basic config data.
basic_cfg = load_json(r"config\basic_cfg.json")
WEBSITE_TITLE = "website_title"
LOGO_IMG = "logo_img"
APP_START_TEXT = "app_start_text"


## App definition
app = Flask(__name__)

@app.route('/')
def root():
    return redirect("/Home")

@app.route('/<page_name>')
def other(page_name):
    return render_template(
        f'{page_name}.html', 
        page_name = page_name,
        website_title = basic_cfg[WEBSITE_TITLE],
        logo_img = basic_cfg[LOGO_IMG]
    )



## App Running...
if __name__ == '__main__':
    Logger.log_info(basic_cfg[APP_START_TEXT])
    app.run()