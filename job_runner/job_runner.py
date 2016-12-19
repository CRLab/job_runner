import os
from multiprocessing import Process, Queue
import multiprocessing
import argparse
import importlib


def task_loop(task_queue, job_runner_class):
    print "In Task Queue"

    worker = job_runner_class()

    print "constructed worker"
    while True:
        msg = task_queue.get()
        if msg == 'DONE':
            break
        else:
            task = msg
            try:
                worker.run_task(task)
            except Exception as e:
              print e
    print "Worker finished"


class JobRunner(object):

    def __init__(self, num_workers=multiprocessing.cpu_count()-2):
        self.num_workers = num_workers

    #Override this function to collect all the tasks to run
    def get_tasks(self):
        raise NotImplementedError()

    # how to run an individual task
    def run_task(self, task):
        raise NotImplementedError()

    def run(self):
        tasks = self.get_tasks()

        task_queue = Queue()

        print("starting readers")
        num_workers = self.num_workers

        readers = []
        for i in range(num_workers):
            reader_p = Process(target=task_loop,
                               args=(task_queue, self.__class__))
            reader_p.daemon = True
            reader_p.start()
            readers.append(reader_p)

        print("putting indices on queue")
        for task in tasks:
            task_queue.put(task)

        print("putting done statements on queue")
        for i in range(num_workers):
            task_queue.put('DONE')

        for reader_p in readers:
            reader_p.join()


if __name__ == "__main__":

    job_runner = JobRunner()
    job_runner.run()
   