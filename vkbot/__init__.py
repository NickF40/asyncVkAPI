from vkbot.vkinterface import *


class VkBot:
    def __init__(self, token):
        self.__token = token
        pass

    def get_updates(self):
        pass

    def polling(self):
        pass

    def process_new_updates(self, update):
        pass
gitgot
    def stop_polling(self):
        pass

    """
    Here'd be decorators like:

     def decorator(handler):
            handler_dict = self._build_handler_dict(handler,
                                                    commands=commands,
                                                    regexp=regexp,
                                                    func=func,
                                                    content_types=content_types,
                                                    **kwargs)

            self.add_message_handler(handler_dict)

            return handler

        return decorator

    !! But we have to find other ways to improve the api !!
    """