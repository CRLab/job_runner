# job_runner

Useful little helper class for running multiprocess jobs using python.  Example

'''
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
    job_runner = PrintJobRunner()
    job_runner.run()
'''
