from timeit import default_timer as timer

def clock(f):
    s = timer()
    assert(f())
    e = timer()
    return (e - s)

def naive_cracK(t, ds):
	for d in ds:
		if t == d:
			return True
		else:
			continue
	return False

def crack_speed(ts, d):
	avs = 0.0
	for t in ts:
		avs += clock(lambda: naive_cracK(t, d))
	return avs / len(ts)

def inter(l1, l2):
    return list(set(l1) & set(l2))

def diff(l1, l2):
    return list(set(l1) - set(l2))
