Python pickle module is used for serializing and de-serializing python object structures. 
The process to converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) is called pickling 
or serialization or flattening or marshalling.
We can converts the byte stream (generated through pickling) back into python objects by a process called as unpickling.


Example:
import pickle
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)