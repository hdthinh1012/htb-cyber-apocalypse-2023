import pickle
import pickletools

aaa = pickle.dumps(['pickle', 'me', 1, 2, 3])

print(aaa)

pickletools.dis(aaa)
