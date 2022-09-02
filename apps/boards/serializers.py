from rest_framework import serializers

from .models import NoticeBoard, FreeBoard, OperationBoard


class NoticeBoardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hit = serializers.IntegerField(read_only=True)

    class Meta:
        model = NoticeBoard
        fields = (
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'updated_at',
            'hit'
        )


class FreeBoardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hit = serializers.IntegerField(read_only=True)

    class Meta:
        model = FreeBoard
        fields = (
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'updated_at',
            'hit'
        )


class OperationBoardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hit = serializers.IntegerField(read_only=True)

    class Meta:
        model = OperationBoard
        fields = (
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'updated_at',
            'hit'
        )
