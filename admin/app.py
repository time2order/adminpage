from flask import Flask, render_template, redirect, url_for, request
import db

app = Flask(__name__)

@app.route("/")
def index():
    vendors = db.get_pending_vendors()
    return render_template("index.html", vendors=vendors)

@app.route("/approve/<int:vendor_id>", methods=["POST"])
def approve(vendor_id):
    vendor = db.get_vendor_by_id(vendor_id)
    if vendor:
        db.insert_into_vendors(vendor)
        db.delete_from_yettoapprove(vendor_id)
    return redirect(url_for("index"))

@app.route("/reject/<int:vendor_id>", methods=["POST"])
def reject(vendor_id):
    vendor = db.get_vendor_by_id(vendor_id)
    if vendor:
        db.insert_into_rejectedlist(vendor)
        db.delete_from_yettoapprove(vendor_id)
    return redirect(url_for("index"))

@app.route('/shops')
def shops():
    vendors =db.get_vendors()
    products = {}
    for vendor in vendors:
        products[vendor['username']] = db.get_products_by_vendor(vendor['username'])
    
    return render_template('shops.html', vendors=vendors, products=products)


@app.route('/shop/<int:vendor_id>')
def shop_detail(vendor_id):
    """Render the shop detail page for a specific vendor."""
    vendor = db.get_vendorapproved_by_id(vendor_id)
    print(vendor)
    if not vendor:
        # Handle case where the vendor is not found
        return render_template('shops_detail.html', vendor=None, products=[])

    products = db.get_products_by_vendor(vendor_id)
    return render_template('shops_detail.html', vendor=vendor, products=products)

if __name__ == "__main__":
    app.run(debug=True)
