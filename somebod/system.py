# -*- coding: utf-8 -*-

import os
import time


def os_query(qry, logger):
    """
        Human wrapper for os.system function

        - Raise OSError if something went wrong
        - Print time elapsed
    """
    start = time.time()
    retval = os.system(qry)
    duration = time.time() - start
    if retval:
        logger.error("[%(duration).2fs], retval=%(retval)s, %(qry)s" % locals())
        raise OSError("Cannot execute %(qry)s" % locals())
    else:
        logger.info("[%(duration).2fs], retval=%(retval)s, %(qry)s" % locals())
