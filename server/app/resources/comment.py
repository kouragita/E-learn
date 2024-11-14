from flask_restful import Resource, reqparse
from app.models import db
from app.models.comment import Comment
from app.schemas.comment_schema import CommentSchema

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

class CommentResource(Resource):
    def get(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        return comment_schema.dump(comment), 200

    def put(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        parser = reqparse.RequestParser()
        parser.add_argument('content', type=str, required=True)
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('resource_id', type=int, required=True)
        args = parser.parse_args()

        comment.content = args['content']
        comment.user_id = args['user_id']
        comment.resource_id = args['resource_id']
        db.session.commit()
        return comment_schema.dump(comment), 200

    def delete(self, comment_id):
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()
        return {'message': 'Comment deleted'}, 204

class CommentListResource(Resource):
    def get(self):
        comments = Comment.query.all()
        return comments_schema.dump(comments), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('content', type=str, required=True)
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('resource_id', type=int, required=True)
        args = parser.parse_args()

        comment = Comment(
            content=args['content'],
            user_id=args['user_id'],
            resource_id=args['resource_id']
        )
        db.session.add(comment)
        db.session.commit()
        return comment_schema.dump(comment), 201
