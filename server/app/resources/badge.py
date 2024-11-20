# from flask_restful import Resource, reqparse
# from app.models import db
# from app.models.badge import Badge
# from app.schemas.badge_schema import BadgeSchema

# badge_schema = BadgeSchema()
# badges_schema = BadgeSchema(many=True)

# class BadgeResource(Resource):
#     def get(self, badge_id):
#         badge = Badge.query.get_or_404(badge_id)
#         return badge_schema.dump(badge), 200

#     def put(self, badge_id):
#         badge = Badge.query.get_or_404(badge_id)
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str, required=True)
#         parser.add_argument('description', type=str, required=True)
#         parser.add_argument('image_url', type=str)
#         parser.add_argument('points_required', type=int, required=True)
#         args = parser.parse_args()

#         badge.name = args['name']
#         badge.description = args['description']
#         badge.image_url = args.get('image_url', badge.image_url)
#         badge.points_required = args['points_required']
#         db.session.commit()
#         return badge_schema.dump(badge), 200

#     def delete(self, badge_id):
#         badge = Badge.query.get_or_404(badge_id)
#         db.session.delete(badge)
#         db.session.commit()
#         return {'message': 'Badge deleted'}, 204

# class BadgeListResource(Resource):
#     def get(self):
#         badges = Badge.query.all()
#         return badges_schema.dump(badges), 200

#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str, required=True)
#         parser.add_argument('description', type=str, required=True)
#         parser.add_argument('image_url', type=str)
#         parser.add_argument('points_required', type=int, required=True)
#         args = parser.parse_args()

#         badge = Badge(
#             name=args['name'],
#             description=args['description'],
#             image_url=args.get('image_url'),
#             points_required=args['points_required']
#         )
#         db.session.add(badge)
#         db.session.commit()
#         return badge_schema.dump(badge), 201

from flask_restful import Resource, reqparse
from app.models import db
from app.models.badge import Badge
from app.schemas.badge_schema import BadgeSchema

badge_schema = BadgeSchema()
badges_schema = BadgeSchema(many=True)

class BadgeResource(Resource):
    def get(self, badge_id):
        badge = Badge.query.get(badge_id)
        if not badge:
            return {"error": "Badge not found"}, 404
        return badge_schema.dump(badge), 200

    def put(self, badge_id):
        badge = Badge.query.get_or_404(badge_id)
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('image_url', type=str)
        parser.add_argument('points_required', type=int, required=True, help="Points must be a positive integer")
        args = parser.parse_args()

        badge.name = args['name']
        badge.description = args['description']
        badge.image_url = args.get('image_url', badge.image_url)
        badge.points_required = args['points_required']
        db.session.commit()
        return badge_schema.dump(badge), 200

    def delete(self, badge_id):
        badge = Badge.query.get_or_404(badge_id)
        db.session.delete(badge)
        db.session.commit()
        return {'message': 'Badge deleted'}, 204


class BadgeListResource(Resource):
    def get(self):
        badges = Badge.query.all()
        return {
            "count": len(badges),
            "badges": badges_schema.dump(badges)
        }, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('image_url', type=str)
        parser.add_argument('points_required', type=int, required=True, help="Points must be a positive integer")
        args = parser.parse_args()

        badge = Badge(
            name=args['name'],
            description=args['description'],
            image_url=args.get('image_url'),
            points_required=args['points_required']
        )
        db.session.add(badge)
        db.session.commit()
        return badge_schema.dump(badge), 201
