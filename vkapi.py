import vk

session = vk.Session()
api = vk.API(session, v=5.0)

def send_message(user_id, token, message, buttons, attachment=""):
    if buttons == None:
        api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)
    else:
        api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment, keyboard = buttons)