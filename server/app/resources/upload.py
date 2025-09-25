from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import jwt_required
from app.services.cloudinary_service import CloudinaryService

class FileUploadResource(Resource):
    @jwt_required()
    def post(self):
        if 'file' not in request.files:
            return {"message": "No file part"}, 400
        
        file = request.files['file']

        if file.filename == '':
            return {"message": "No selected file"}, 400

        if file:
            try:
                cloudinary_service = CloudinaryService()
                upload_result = cloudinary_service.upload_file(file)
                return {
                    "message": "File uploaded successfully",
                    "url": upload_result.get('secure_url'),
                    "public_id": upload_result.get('public_id')
                }, 201
            except Exception as e:
                return {"message": str(e)}, 500
        
        return {"message": "File upload failed"}, 400
