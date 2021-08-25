from Action.models import Action
from Action.serializers import ActionSerializer
from Logger.serializers import LoggerSerializer


def log(name, type, visible, user, id):
    action = Action.objects.get(name=name)
    actionSerialzer = ActionSerializer(action)
    log = {
        'action': actionSerialzer.data['id'],
        'is_visible': visible,
        'type': type,
        'reference': id,
    }
    print(log)
    loggerSerializer = LoggerSerializer(data=log)
    if loggerSerializer.is_valid():
        loggerSerializer.save(
            created_by=user
        )
