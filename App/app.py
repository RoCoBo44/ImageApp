from flask import Flask, render_template, request
import requests
import validators
import uuid
from PIL import Image
import base64
from io import BytesIO

def create_app():

  app = Flask(__name__)

  IMAGE_DICT = {}
  VALID_IMAGE_EXTENSIONS = [
      ".jpg",
      ".jpeg",
      ".png",
      ".gif",
  ]

  def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSIONS):
      return any([url.endswith(e) for e in extension_list])

  @app.route("/")
  def home():
      return render_template("upload_image.html")

  @app.route("/upload_image")
  def upload_image():
      return render_template("upload_image.html")

  @app.route("/upload_result", methods=["POST"])
  def upload_result():

      #take image and url 
      image_req = request.files['image']
      url_req = request.form.get('url')

      #validate everthing is ok
      if not image_req and not url_req:
        return render_template("error.html", message="Missing image")
      if image_req:
        image = Image.open(image_req)
      elif validators.url(url_req) and valid_url_extension(url_req):
        image = Image.open(requests.get(url_req, stream=True).raw)
      else:
        return render_template("error.html", message="Not valid URL")

      #save image in base64 and with unique id
      data = BytesIO()
      image.save(data, "PNG")
      encoded_img_data = base64.b64encode(data.getvalue())
      image_id = str(uuid.uuid4())
      IMAGE_DICT[image_id] = encoded_img_data #save the b64 image and unique-key 
      return render_template("success.html", id = image_id)

  @app.route("/analyse_image", methods=["GET", "POST"])
  def analyse_image():
      if request.method == 'GET':
        return render_template("analyse_image.html")
      
      image_id = request.form.get("image_id")
      
      #validate if it has id
      if not image_id:
        return render_template("error.html", message="Not given image_id")
      
      imageB64 = IMAGE_DICT.get(image_id)
      
      #validate id in dictionary 
      if not imageB64:
        return render_template("error.html", message="The id is not correct")

      #transform base64 to pil (also help with future things)
      im_bytes = base64.b64decode(imageB64)   
      im_file = BytesIO(im_bytes) 
      img = Image.open(im_file)   
      width, height = img.size
      return render_template("analyse_image.html", width= width,height= height)


  @app.route("/list_images")
  def list_images():
      return render_template("list_images.html", image_dict=IMAGE_DICT)

  return app
