from django.shortcuts import render
from uuid import UUID
from django.core.serializers.json import Serializer as JSONSerializer

def ValidateUUID(uuid):
    try:
        UUID(uuid,version=4)
    except:
        return False
    return True

class FieldsJSONSerializer(JSONSerializer):
    def get_dump_object(self, obj):
        dump_object = {'pk': obj._get_pk_val()}
        dump_object.update(self._current or {})
        return dump_object