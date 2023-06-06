import click

@click.command(help="This is just a hello app. It does nothing.")

def toyou(x):
    return "hi %s" % x


def add(x):
    return x + 1


def subtract(x):
    return x - 1