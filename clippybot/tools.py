import hashlib
import os
from shutil import copy2 as copy
import hashlib
from functools import partial



def md5(filename, chunksize=2**15, bufsize=-1):
    m = hashlib.md5()
    with open(filename, 'rb', bufsize) as f:
        for chunk in iter(partial(f.read, chunksize), b''):
            m.update(chunk)
    return m.hexdigest()

def copy_file(source, dest, dry_run=False):
    if dry_run:
        LOG.warning('Copy file : %s' % dest)
    else:
        LOG.info('Copy file : %s' % dest)
        copy(source, dest)


def check_file_consistency(source, dest, dry_run=False):
    if dry_run:
         LOG.warning('Check file consistency between %s -> %s' % (source, dest))
         return True
    else:
        LOG.info('Check file consistency between %s -> %s' % (source, dest))
        sum_source = md5(filename=source)
        sum_dest = md5(filename=dest)
        LOG.debug('Sum : %s %s' % (sum_source, sum_dest))
        if sum_source != sum_dest: return False
        else: return True
