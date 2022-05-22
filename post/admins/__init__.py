from django.contrib import admin

from post.admins.post import PostAdmin
from post.admins.comment import CommentAdmin

from post.models import (
    Post as PostModel,
    Comment as CommentModel,
)

admin.site.register(PostModel, PostAdmin)
admin.site.register(CommentModel, CommentAdmin)



