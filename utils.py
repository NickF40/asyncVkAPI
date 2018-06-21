import asyncio
import multiprocessing
import threading

try:
	import Queue
except ImportError:
	import queue as Queue


"""
Base class for storing running Bot instances
ToDo:
- think over some memory\database instances, that may be the issue of "memory race"
"""
class WorkProcess:
	def __init__(self):
		pass

	def run(self):
		pass

	def stop(self):
		pass


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

"""
Session class, that provides saving user information & connecting multiply accounts from different messengers & sn
Todo:
- rewrite some methods with dunder-functions
"""
class Session:
	def __init__(self, user_id, **kwargs):
		self.user_id = user_id
		self.data = {} if not kwargs else dict(kwargs)

	def pause(self, device):
		pass

	def new(self. device):
		pass

	def remove(self, device):
		pass

