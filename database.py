from sqlalchemy import create_engine,text
#Remove or comment this line before pushing to github.
# from dotenv import load_dotenv 
import os

#Remove or comment this line before pushing to github.
# load_dotenv() 

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    },
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    return jobs
  
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f'SELECT * FROM jobs WHERE id = {id}'))

  rows = result.all()
  if len(rows) == 0:
    return None
  else:
    return rows[0]._asdict()


