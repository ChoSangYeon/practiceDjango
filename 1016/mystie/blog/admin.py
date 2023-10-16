from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at']
    # fields = ['title', 'content'] # 이전 버전에서는 fields를 사용했습니다.

admin.site.register(Post, PostAdmin)
# 자주 쓰기 때문에 안 보고도 쓸 줄 알아야 합니다.