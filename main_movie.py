from naver_movie import get_movie_comm as get_comm
import os
import time
from concurrent.futures import ThreadPoolExecutor


with ThreadPoolExecutor(max_workers=5) as executor:
    # executor.submit(get_comm, 172816)
    for i in range(153862, 153865):
        executor.submit(get_comm, i)