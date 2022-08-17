from project_management.source.models.comment import Comment


def get_comments(work_id):
    return list(Comment.objects(work_id=work_id))


def get_comment(comment_id):
    return Comment.objects(id=comment_id).first()


def create_comment(comment):
    new_comment = Comment(comment=comment["comment"], work_id=comment["work_id"])
    new_comment.save()
    return str(new_comment.id)


def update_comment(comment_id, comment):
    comment_object = Comment.objects(id=comment_id).first()
    if comment_object:
        comment_object.comment = comment["comment"]
        comment_object.save()
    return comment_object


def delete_comment(comment_id):
    comment_object = Comment.objects(id=comment_id).first()
    if comment_object:
        comment_object.is_deleted = True
        comment_object.save()
        return str(comment_object.id)
    else:
        return False
