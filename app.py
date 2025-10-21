from flask import Flask, render_template
from pathlib import Path
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events-aby-goa') #12032020
def events():
    return render_template('events.html')

@app.route('/invitation')
def invitation():
    return render_template('aby_invitation.html')

@app.route('/when-where')
def location():
    return render_template('when-where.html')

@app.route('/rsvp')
def rsvp():
    return render_template('goa_rsvp.html')

@app.route('/photo-gallery')
def gallery():
    gallery_dir = Path(app.static_folder) / "images/photo-gallery"
    image_names = sorted(
        name for name in os.listdir(gallery_dir)
        if name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.heic'))
    )
    image_urls = [f"images/photo-gallery/{name}" for name in image_names]
    print("#"*100)
    print(image_urls)
    return render_template('gallery.html', gallery_images=image_urls)

if __name__ == '__main__':
    app.run(debug=True)