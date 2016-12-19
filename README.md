# job_runner

Very lightweight tool for python multiprocessing.  Just override get_tasks to create a dictionary of tasks.  And run_task to specify how a single task should be run. You can also specify how many workers to run, default is n-2 of however many cores your machine has. Each worker is its own process.

Example

```
import job_runner


class PrintJobRunner(job_runner.JobRunner):

    def get_tasks(self):
        tasks = []
        for i in range(100):
            tasks.append({'i': i})
        return tasks

    def run_task(self,task):
        print task

if __name__ == "__main__":
    job_runner = PrintJobRunner(num_workers=4)
    job_runner.run()
```
