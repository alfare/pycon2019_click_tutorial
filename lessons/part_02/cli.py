#!/usr/bin/env python

import click


@click.command()
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
# @click.option('--red', is_flag=True)
def cli(infile, outfile):
    """
    if red:
        click.secho('Hello!', fg='red')
        click.secho('Printing...', fg='red', err=True)
    else:
        click.echo('Hello!')
        click.echo('Printing...', err=True)
    """
    input_data = infile.read()
    input_data_length = len(input_data)
    click.echo(input_data, file=outfile, nl=False)
    click.echo(f'Input length: {input_data_length}', err=True)


if __name__ == "__main__":
    cli()
