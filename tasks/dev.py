from invoke import task


@task(default=True)
def dev(context):
    """
    Start dev server
    """
    from app import start_server
    server = start_server()
    return server.run()
