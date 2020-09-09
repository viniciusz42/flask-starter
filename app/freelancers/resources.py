import os
from flask import request
from flask_restplus import Resource, Namespace, fields, marshal_with
from .schemas import FreelancerSchema
from .business import sum_freelancer_hours
from app.core.errorhandler import ErrorHandler

ns = Namespace("Freelancer Namespace", url_prefix="/", description="")

@ns.route("freelancer")
class Freelancer(Resource):
    def post(self):
        try:
            payload = FreelancerSchema().load(request.json)
            results = sum_freelancer_hours(payload)
            return results, 200

        except Exception as error:
            return ErrorHandler(error).handle()
