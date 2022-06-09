import multiprocess as mp
import pandas as pd

def get_jobs(df):
  jobs = list()
  for row in df.iterrows():
    job = (row.a, row.b, row.c)
    jobs.append(job)
  return jobs

def process(task):
  pass
  # do something

def parallel_process(jobs):
  pool = mp.Pool(mp.cpu_count()-1)
  pool.map(process, jobs)
  pool.close()
  pool.join()

if __name__ == '__main__':
  df = pd.read_csv('path to file')
  jobs = get_jobs(df)
  parallel_process(jobs)
  
