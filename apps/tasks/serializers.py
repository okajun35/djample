
from rest_framework import serializers

from accounts.models import User
from accounts.serializers import UserSerializer
from .models import Status, Tag, Task, Time


class StatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')
        extra_kwargs = {}


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name', 'description')
        extra_kwargs = {}


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)
        extra_kwargs = {}


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'user', 'group', 'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'write_only': True},
            'updated_at': {'write_only': True},
        }


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('id', 'task', 'note', 'start', 'end')
        extra_kwargs = {}


class TimeListSerializer(serializers.ListSerializer):
    child = TimeSerializer()

    class Meta:
        model = Time
        fields = ('id', 'status', 'content', 'owner')
        extra_kwargs = {}


class TaskSerializer(serializers.ModelSerializer):
    # times = TimeSerializer(many=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.filter(),
        many=True, required=False,
    )

    tags = TagSerializer(many=True, required=False)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.filter(),
        many=True, required=False,
        source='tags'
    )
    owner = UserSerializer(required=False)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(),
        source='owner'
    )
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.filter(),
        source='status'
    )
    status = StatusSerializer(required=False)

    class Meta:
        model = Task
        fields = (
            'id', 'content', 
            'tags', 
            'tag_ids',
            'owner', 
            'owner_id',
            'status',
            'status_id',
            'created_at', 'updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'times': {'write_only': True},
            'tags': {'read_only': True},
            'tag_ids': {'write_only': True},
            'owner': {'read_only': True},
            'status': {'read_only': True},
            'status_id': {'write_only': True},
        }


class TaskListSerializer(serializers.ListSerializer):
    child = TaskSerializer()
