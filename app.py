from flask import Flask, render_template, request, send_file, send_from_directory, url_for, redirect
from qr_utils import get_qr_bytes
import io
import base64

app = Flask(__name__)

# Register b64encode filter for Jinja2
@app.template_filter('b64encode')
def b64encode_filter(data):
    """Encode binary data to base64 for embedding in HTML."""
    return base64.b64encode(data).decode('utf-8')

# Serve JS files from scripts/
@app.route('/scripts/<path:filename>')
def serve_script(filename):
    return send_from_directory('scripts', filename)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("qrtext", "")
        # Redirect to GET with query param to prevent QR persistence on refresh
        return redirect(url_for("index", qrtext=text))

    # GET request
    text = request.args.get("qrtext", "")
    qr_img = get_qr_bytes(text) if text else None
    return render_template("index.html", qr_img=qr_img, qrtext=text)

@app.route("/download", methods=["POST"])
def download():
    text = request.form.get("qrtext")
    img_bytes = get_qr_bytes(text)
    return send_file(io.BytesIO(img_bytes), mimetype="image/png", as_attachment=True, download_name="qr.png")

if __name__ == "__main__":
    app.run(debug=True)
