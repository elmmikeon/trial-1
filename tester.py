from queue import Queue
from threading import Thread
import copy

# Object that signals shutdown
_sentinel = object()

# increment function
def increment(i, out_q):
    i += 1
    print(i)
    out_q.put(i)
    return

# A thread that produces data
def producer(out_q):
    i = 0
    while True:
        # Produce some data
        increment( i , out_q)

        if i > 5:
            out_q.put(_sentinel)
            break

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data

        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()



# Wait for all produced items to be consumed
q.join()