import sys
import tornado

collect_ignore = []
if sys.version_info[:2] < (3, 5):
    collect_ignore.append("test_async_await.py")
