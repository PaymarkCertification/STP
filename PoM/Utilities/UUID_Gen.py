import uuid

def randUUID() ->int:
    return uuid.uuid1()
    
print(randUUID())