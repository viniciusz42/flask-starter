from invoke import task


@task(default=True)
def test(context):
    """
    Run unit tests
    """
    context.run("nose2 -v --pretty-assert")
