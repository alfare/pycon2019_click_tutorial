#!/usr/bin/env python

import click


@click.command()
@click.argument('names', nargs=-1)
@click.option('--greeting', '-g', default='Hello', help='The greeting to display')
@click.option('--question', '-q', is_flag=True, help='Make the greeting a question')
@click.option('--int-option', type=int)
@click.option('--float-option', type=float)
@click.option('--bool-option', type=bool)
@click.option('--choice-option', type=click.Choice(['A', 'B', 'C']))
def cli(names, greeting, question, int_option, float_option, bool_option, choice_option):
    """Displays a greeting."""
    punctuation = '!'
    if question:
        punctuation = '?'
    for name in names:
        print(f'{greeting}, {name}{punctuation}')
    print_option('int', int_option)
    print_option('float', float_option)
    print_option('bool', bool_option)
    print_option('choice', choice_option)


def print_option(option, value):
    if option is not None:
        print(f'{option}: {value}')


if __name__ == "__main__":
    cli()
