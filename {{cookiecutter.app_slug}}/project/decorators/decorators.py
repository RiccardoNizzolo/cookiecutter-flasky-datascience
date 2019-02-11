import logging
log=logging.getLogger('console')

def timer(f):
    import timeit
    def wrapped(*args, **kwargs):
        tic = timeit.default_timer()
        ret = f(*args, **kwargs)
        toc = timeit.default_timer()
        log.info("runned %s in %s s",f.__name__,toc-tic)
        return ret
    return wrapped