import click

UP_ARROW_KEY = "\00H"
DOWN_ARROW_KEY = "\00P"


def navigate(current_index, max_items):
    new_index = current_index
    key = click.getchar()

    if key == UP_ARROW_KEY:
        new_index = (current_index - 1)
    elif key == DOWN_ARROW_KEY:
        new_index = (current_index + 1)

    return new_index % max_items
