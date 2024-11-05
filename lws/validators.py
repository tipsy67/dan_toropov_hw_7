from rest_framework import serializers


class URLCustomValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        data = value.get(self.field)
        if data is not None:
            if not 'youtube.com' in data.lower():
                raise serializers.ValidationError({self.field:'Запрещены ссылки на сторонние ресурсы'})