from flask import Blueprint

admin_bp = Blueprint('admin_api', __name__)

def register_admin_routes(api):
    from .resources.content_management import (
        AdminLearningPathListResource, AdminLearningPathResource,
        AdminModuleListResource, AdminModuleResource,
        AdminResourceListResource, AdminResourceResource,
        AdminLearningPathModulesResource, AdminModuleResourcesResource
    )
    from .resources.upload import AdminUploadSignatureResource
    from .resources.quiz_resources import AdminQuizListResource, AdminQuizResource, AIQuizGenerateResource
    from .resources.integrations import UssdLogsResource, SmsLogsResource, SmsBroadcastResource

    # Admin Routes
    api.add_resource(AdminLearningPathListResource, '/api/admin/learning_paths')
    api.add_resource(AdminLearningPathResource, '/api/admin/learning_paths/<int:path_id>')
    api.add_resource(AdminLearningPathModulesResource, '/api/admin/learning_paths/<int:path_id>/modules')
    api.add_resource(AdminModuleListResource, '/api/admin/modules')
    api.add_resource(AdminModuleResource, '/api/admin/modules/<int:module_id>')
    api.add_resource(AdminModuleResourcesResource, '/api/admin/modules/<int:module_id>/resources')
    api.add_resource(AdminResourceListResource, '/api/admin/resources')
    api.add_resource(AdminResourceResource, '/api/admin/resources/<int:resource_id>')
    # Upload Routes
    api.add_resource(AdminUploadSignatureResource, '/api/admin/upload/signature')

    # Quiz Routes
    api.add_resource(AdminQuizListResource, '/api/admin/modules/<int:module_id>/quizzes')
    api.add_resource(AdminQuizResource, '/api/admin/quizzes/<int:quiz_id>')
    api.add_resource(AIQuizGenerateResource, '/api/admin/ai/generate-quiz')

    # Integrations Routes
    api.add_resource(UssdLogsResource, '/api/admin/integrations/ussd-logs')
    api.add_resource(SmsLogsResource, '/api/admin/integrations/sms-logs')
    api.add_resource(SmsBroadcastResource, '/api/admin/integrations/broadcast')
