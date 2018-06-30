import asyncio
import multiprocessing
import threading

try:
    import Queue
except ImportError:
    import queue as Queue

"""
WorkThread class: basic class for separating some parts of bot instance
"""


class WorkThread(threading.Thread):
    def __init__(self):
        pass

    def run(self):
        pass

    def put(self):
        pass

    def stop(self):
        pass


class ThreadPool:
    def __init__(self):
        pass

    def put(self):
        pass

    def close(self):
        pass


"""
Basic class for starting async tasks
Need to look through Github: aioprocessing for better understanding

Todo:
- rewrite special func for aiohttp for requests
- think over other instances, that may need async tasks
- check possibility for running async connection with each user, stored in sessions
"""


class AsyncTask:
    def __init__(self):
        pass

    def _run(self):
        pass

    def wait(self):
        pass
