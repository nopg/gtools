from flask import Flask, render_template, url_for, flash, redirect, Markup
import forms

import bs_maker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'


@app.route("/", methods=["GET"])
def index():
    # Create Form
    return render_template("index.html", title="gMenu")


@app.route("/bs_maker", methods=["GET", "POST"])
def bs_create():
    # Create Form
    form = forms.BS_CreatePage()

    # Submit:
    if form.validate_on_submit():
        # Gather Args
        kwargs = {
                    'private_subnet':form.private_subnet.data,
                    'web_subnet':form.web_subnet.data,
                    'db_subnet':form.db_subnet.data,
                    'business_subnet':form.business_subnet.data,

                    'hostname1':form.pahostname1.data,
                    'public_ip1':form.papublicip1.data,
                    'public_nexthop1':form.papublicnexthop1.data,
                    'private_ip1':form.paprivateip1.data,
                    'private_nexthop1':form.paprivatenexthop1.data,

                    'hostname2':form.pahostname2.data,
                    'public_ip2':form.papublicip2.data,
                    'public_nexthop2':form.papublicnexthop2.data,
                    'private_ip2':form.paprivateip2.data,
                    'private_nexthop2':form.paprivatenexthop2.data,

                    'storage_account_name':form.storage_account_name.data,
                    'storage_folder_name':form.storage_folder_name.data,
                    'storage_access_key':form.storage_access_key.data
        }
        # Update bootstrap, alert user.
        msg, successOrFail = bs_maker.create_lb_bootstrap('static/bs-template1.xml', 'static/bs-template2.xml', **kwargs)

        flash(msg, successOrFail)

    return render_template("bs_create.html", title="PA Bootstrap Maker", form=form)

@app.route("/az_arms", methods=["GET"])
def az_arms():
    return render_template("az_arms.html", title="Azure ARM Templates")


@app.route("/about")
def about():
    return render_template("temp.html", title="gAbout")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("temp.html", title="gMenu")


@app.route("/uvu", methods=["GET", "POST"])
def login():
    return render_template("uvu/uvu.html", title="Utah Valley University!")


# If run from the command line
if __name__ == "__main__":
    app.run(debug=True)