from project_management.source.models.project import Project


def get_project_works_comments():
    pipeline = [
                {
                    '$lookup': {
                        'from': 'work',
                        'localField': '_id',
                        'foreignField': 'project_id',
                        'as': 'works'
                    }
                }, {
                    '$unwind': {
                        'path': '$works',
                        'preserveNullAndEmptyArrays': True
                    }
                }, {
                    '$lookup': {
                        'from': 'comment',
                        'localField': 'works._id',
                        'foreignField': 'work_id',
                        'as': 'works.comments'
                    }
                }, {
                    '$group': {
                        '_id': '$_id',
                        'name': {
                            '$first': '$name'
                        },
                        'state': {
                            '$first': '$state'
                        },
                        'created_at': {
                            '$first': '$created_at'
                        },
                        'works': {
                            '$push': '$works'
                        }
                    }
                }
            ]
    return Project.objects().aggregate(pipeline)
