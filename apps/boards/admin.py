from django.contrib import admin

from . import models


@admin.register(models.NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'content',
        'created_at',
        'updated_at',
        'hit',
    )


@admin.register(models.FreeBoard)
class FreeBoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'content',
        'created_at',
        'updated_at',
        'hit',
    )


@admin.register(models.OperationBoard)
class OperationBoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'content',
        'created_at',
        'updated_at',
        'hit',
    )
