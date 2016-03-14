from rest_framework import serializers
from sentry.models.host_stream import Stream, StreamType, HostType, Tag, LogEvent, LogFile


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name', 'user', )


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = ('id', 'stream_name', 'stream_type', 'host', 'tag', )


class HostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostType
        fields = ('id', 'host_type', )


class StreamTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamType
        fields = ('id', 'stream_type', )


class LogFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogFile
        fields = ('id', 'host', 'file_path', 'file_name', 'create_timestamp', 'modify_timestamp', )


class LogEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEvent
        fields = ('id', 'payload', 'offset', 'user', 'LogFile', )
