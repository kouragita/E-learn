import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import current_app
import time

class CloudinaryService:
    @staticmethod
    def upload_file(file, folder='elearn/', resource_type='auto'):
        """
        Upload file to Cloudinary
        :param file: File object or URL
        :param folder: Cloudinary folder path
        :param resource_type: Type of resource (image, video, raw)
        :return: Upload result dictionary
        """
        try:
            result = cloudinary.uploader.upload(
                file,
                folder=folder,
                resource_type=resource_type,
                overwrite=True,
                invalidate=True
            )
            return result
        except Exception as e:
            raise Exception(f"Cloudinary upload failed: {str(e)}")
    
    @staticmethod
    def delete_file(public_id, resource_type='image'):
        """
        Delete file from Cloudinary
        :param public_id: Cloudinary public ID
        :param resource_type: Type of resource
        :return: Deletion result
        """
        try:
            result = cloudinary.uploader.destroy(
                public_id,
                resource_type=resource_type
            )
            return result
        except Exception as e:
            raise Exception(f"Cloudinary deletion failed: {str(e)}")
    
    @staticmethod
    def generate_upload_signature():
        """
        Generate secure upload signature for direct uploads
        :return: Signature dictionary
        """
        timestamp = int(time.time())
        signature = cloudinary.utils.api_sign_request(
            {
                "timestamp": timestamp,
                "folder": "elearn/uploads"
            },
            current_app.config['CLOUDINARY_API_SECRET']
        )
        
        return {
            "signature": signature,
            "timestamp": timestamp,
            "api_key": current_app.config['CLOUDINARY_API_KEY'],
            "folder": "elearn/uploads"
        }