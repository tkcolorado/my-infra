from fabric import task

@task
def uname(c):
    """Execute uname."""
    result = c.run("uname -n", hide=True)
    print(result.stdout.strip())