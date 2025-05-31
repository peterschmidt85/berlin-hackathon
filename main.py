import sys

from dstack.api import Task, Client, LocalRepo

client = Client.from_config()

task = Task(
    name="test",
    commands=[
        "find .",
    ],
)

repo = LocalRepo(repo_dir=".", repo_id="berlin-hackathon")
client.repos.init(repo)

run = client.runs.apply_configuration(configuration=task, repo=repo)

run.attach()

try:
    for log in run.logs():
        sys.stdout.buffer.write(log)
        sys.stdout.buffer.flush()
except KeyboardInterrupt:
    run.stop(abort=True)
finally:
    run.detach()
