from flask import Response, request, make_response, send_from_directory, send_file
from flask import current_app as app
from flask_restful import Resource
from errors import InternalServerError, SchemaValidationError, UserNotFoundError, EmailAlreadyExistError

import requests
import io
import os

images = [
  'https://hlsatest.s3.amazonaws.com/andrea-de-santis-Iou_Ai4zMCM-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/christian-cueni-f7F-2DL1W_M-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/daniel-sessler-ra8N8QWwQfo-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/danielle-stein-2mTukWMcT30-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/denise-schuld-57RQVUtnDZk-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/eberhard-grossgasteiger-Y3H3vhg2bdk-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/eduardo-dutra-f9mD2TBbWMY-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/jeremy-hynes-XBm7P2Amm2g-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/photo-1633113088942-99089f4abffa.jpg',
  'https://hlsatest.s3.amazonaws.com/priscilla-du-preez-dKrIgSUr4MY-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/rafael-garcin-omP3tOe_NZs-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/ryan-ancill-aJYO8JmVodY-unsplash.jpg',
  'https://hlsatest.s3.amazonaws.com/yiran-ding-NDXJXVh8S7w-unsplash.jpg'
]

class GalleryApi(Resource):

    def get(self, id=None):
        if not id:
          return Response(status=500)

        iid = int(id.split(".")[0])
        if iid >= len(images) or iid < 0:
            return Response(status=500)

        r = requests.get(images[iid])

        r.raise_for_status()
        image_raw = io.BytesIO(r.content)
        
        image_raw.seek(0) # this may not be needed
        buffer = image_raw.read()

        return make_response(send_file(
                  io.BytesIO(buffer),
                  mimetype='image/jpeg',
                  as_attachment=True,
                  attachment_filename=id))

        #response = make_response(buffer)
        #response.headers.set('Content-Type', 'image/jpeg')
        #response.headers.set(
        #    'Content-Disposition', 'attachment', filename=id)
        #
        #return response
        
        #sp = os.path.join(app.root_path,'static') 
        #
        #return make_response(send_from_directory(
        #  sp, '0.jpg', as_attachment=True, mimetype='image/jpeg'
        #))

    def delete(self, id):
      return {"success": True}, 200

