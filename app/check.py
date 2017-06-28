import redis
import sys


r = redis.StrictRedis(host='localhost')
count = 50

def add_word(r, word):
    for l in range(1, len(word)):
        prefix = word[0:l]
        r.zadd('words', 0, prefix)
    r.zadd('words', 0, word+'%')


def complete(r, prefix, count):
	results = set()
	grab = 42
	start = r.zrank('words', prefix)
	if not start:
		return results
	while (len(results) != count):
		range = r.zrange('words', start, start+grab-1)
		start += 1
		if not range or len(range) == 0:
			break
		for entry in range:
			entry = entry.decode("utf-8")
			minlen = min(len(entry), len(prefix))
			if entry[0:minlen] != prefix[0:minlen]:
				count = len(results)
				break
			if entry[-1] == "%" and len(results) != count:
				results.add(entry[0:-1])
	return results


def autoComplete():
	x = complete(r, sys.argv[1], count)
	print(type(x))
	print(x)

if __name__ == "__main__":
	autoComplete()