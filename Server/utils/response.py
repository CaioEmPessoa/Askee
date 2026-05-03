
def build(status, message, data=None):
    return {
        "status": status,
        "message": message,
        "data": data if data is not None else {}
    }
