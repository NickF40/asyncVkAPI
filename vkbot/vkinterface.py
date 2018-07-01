"""
There would be realizations of all methods from VK API,
but we have to look after awaits and so on
concurrent programming, blackjack and whores

"""

import asyncio
import time
import aiohttp

API_URL = 'https://api.vk.com/method/'
TIMEOUT = 0.1


class VkInterface:
    __slots__ = ('token', 'secret_key', 'session', 'queue')

    def __init__(self, token, secret_key):

        self.session = aiohttp.ClientSession()


class RequestsQueue:
    __slots__ = ("vk_client", "queue", "locked", "released", "in_process")

    def __init__(self, vk_client):

        self.vk_client = vk_client

        self.locked = False
        self.released = False
        self.in_process = False

        self._requests_done = 0

        self.queue = asyncio.Queue()

    def get_nowait(self):
        return self.queue.get_nowait()

    def put_nowait(self, data):
        return self.queue.put_nowait(data)

    def __len__(self):
        return self.queue.qsize()

    async def update_queue_processor(self, redo=False):
        """Create a queue processor or update it's state"""

        if not self.processing or redo:
            self.released = False
            self.in_process = True

            asyncio.ensure_future(self.queue_processor())

        if not self.locked or self.requests > 24:
            self.released = True

    async def queue_processor(self):
        try:
            await self._queue_processor()
        except Exception:
            import traceback
            traceback.print_exc()

    async def _queue_processor(self):
        for _ in range(4):
            await asyncio.sleep(TIMEOUT)

            if self.release:
                break

        if self.requests_done > 2:
            wait_time = self.requests_done_clear_time - time.time() + 0.05

            if wait_time > 0: await asyncio.sleep(wait_time)

            return await self.update_queue_processor(True)

        elif self.requests:
            await self.execute_queue()

            if self.requests:
                return await self.update_queue_processor(True)

        self.processing = False

    async def enqueue(self, task):
        if not task:
            return False
        self.queue.put_nowait(task)
        await self.update_queue_processor()
        return True



async def _make_request(token, method_name, method='get', params=None):
    # bla-bla-bla
    pass


def send_message():
    pass


def send_photo():
    pass


def send_file():
    pass


def send_audio():
    pass


def send_location():
    pass


def send_sticker():
    pass


def get_photo():
    pass


def get_file():
    pass


def get_audio():
    pass

# add all other methods here
# automate this process somehow?

