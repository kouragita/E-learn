from flask_restful import Resource
from app.auth.decorators import admin_required
from app.services.cloudinary_service import CloudinaryService

class AdminUploadSignatureResource(Resource):
    method_decorators = [admin_required()]

    def get(self):
        """Generate a secure upload signature for direct uploads to Cloudinary."""
        try:
            signature_data = CloudinaryService.generate_upload_signature()
            return signature_data, 200
        except Exception as e:
            return {"message": str(e)}, 500
