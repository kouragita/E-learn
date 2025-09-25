import cloudinary
import cloudinary.uploader
from flask import current_app

class CloudinaryService:
    def __init__(self):
        self.cloudinary = cloudinary.config(
            cloud_name=current_app.config.get('CLOUDINARY_CLOUD_NAME'),
            api_key=current_app.config.get('CLOUDINARY_API_KEY'),
            api_secret=current_app.config.get('CLOUDINARY_API_SECRET'),
            secure=True
        )

    def upload_file(self, file_to_upload, folder="e-learn-assets"):
        try:
            upload_result = cloudinary.uploader.upload(
                file_to_upload,
                folder=folder,
                resource_type="auto"  # Let Cloudinary detect if it's an image, video, or raw file
            )
            return upload_result
        except Exception as e:
            # In a real app, you'd want more robust logging here
            print(f"Cloudinary upload failed: {e}")
            raise e
