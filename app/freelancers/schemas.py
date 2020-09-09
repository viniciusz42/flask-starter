from marshmallow import Schema, fields, INCLUDE


class SkillSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    name = fields.Str(required=True, allow_none=False)


class FreelancerSkillSchema(Schema):
    id = fields.Int(required=True)
    companyName = fields.Str(required=False, allow_none=True)
    startDate = fields.Str(required=True)
    endDate = fields.Str(required=True)
    skills = fields.List(fields.Nested(SkillSchema))


class FreelanceSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    user = fields.Dict(keys=fields.Str(), values=fields.Str())
    status = fields.Str(required=False, allow_none=True)
    retribution = fields.Int(required=False, allow_none=True)
    availabilityDate = fields.Str(required=False, allow_none=True)
    professionalExperiences = fields.List(fields.Nested(FreelancerSkillSchema))


class FreelancerSchema(Schema):
    freelance = fields.Nested(FreelanceSchema)

    class Meta:
        unknown = INCLUDE
