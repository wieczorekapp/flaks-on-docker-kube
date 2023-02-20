from flask import Flask, jsonify, request, abort
from dict2xml import dict2xml
import json
import yaml

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Visitor(db.Model):
    __tablename__ = "visitors"

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(128), nullable=False)

    def __init__(self, ip):
        self.ip = ip


html_header = """
    <!doctype html>
    <html>
    <head>
    <title>Get your ip address</title>
    <meta name="description" content="get your ip">
    <meta name="keywords" content="ip address">
    </head>
    <body>"""

html_footer = """
    </body>
    </html>"""

@app.route('/')
def client_ip():
    accept = request.headers.get("Accept")
    response = ""

    if accept is not None:
        accept = accept.split(",")
        address_ip = request.environ.get("X-Forwarded-For", request.remote_addr)
        response = {"your_ip": address_ip}
        for i in accept:
            if i.find("/html") != -1:
                response = ""
                response += html_header
                response += f"your_ip: {address_ip}"
                response += html_footer
                break
            elif i.find("/xml") != -1:
                response = dict2xml(response)
                break
            elif i.find("/json") != -1:
                response = jsonify(response)
                break
            elif i.find("/yaml") != -1:
                response = yaml.dump(response)
                break
            elif i.find("/text") != -1:
                response = f"your_ip: {response.get('your_ip')}"
                break
        else:
            abort(406)
    else:
        abort(406)

    db.session.add(Visitor(ip=str(address_ip)))
    db.session.commit()

    return response


@app.get("/history")
def client_ip_history():
    accept = request.headers.get("Accept")
    response = ""

    if accept is not None:
        accept = accept.split(",")
        address_ip = request.environ.get("X-Forwarded-For", request.remote_addr)
        visitors = Visitor.query.all()
        ip_addresses = [str(x.ip) for x in visitors]

        for i in accept:
            if i.find("/html") != -1:
                response = html_header
                for x in ip_addresses:
                    response += f"{x} </br>"

                response += html_footer
                break
            elif i.find("/xml") != -1:
                response = "<ip_history>"
                for x in ip_addresses:
                    response += f"<ip> {x} </ip>"

                response += "</ip_history>"
                break
            elif i.find("/json") != -1:
                response = json.dumps(ip_addresses)
                break
            elif i.find("/yaml") != -1:
                response = yaml.dump(ip_addresses, explicit_start=True, default_flow_style=False)
                break
            elif i.find("/text") != -1:
                response = f"ip_history: {';'.join(ip_addresses)}"
                break
        else:
            abort(406)
    else:
        abort(406)
    
    db.session.add(Visitor(ip=str(address_ip)))
    db.session.commit()

    return response
