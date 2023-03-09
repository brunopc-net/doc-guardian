import os
import log4p

import _hasher as hasher

log = log4p.GetLogger(__name__, config="log4p.json").logger

if __name__ == '__main__':
    log.info(os.listdir("/home/bruno/documents"))
    documents_hash = str(hasher.hash_blake2b(directory='/home/bruno/documents'))
    log.debug("Current documents hash: " + documents_hash)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
