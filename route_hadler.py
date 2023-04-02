from flask import Flask
from Services.service import Short_Url, redirect_url

app = Flask(__name__)
app.add_url_rule("/shortUrl", view_func=Short_Url, methods=["POST"])
app.add_url_rule('/<string:short_id>', view_func=redirect_url, methods=["GET"])

