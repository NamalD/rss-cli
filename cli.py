import click
from models.rss import RssItem
from view import draw, key_input


MAX_ITEMS_PER_SCREEN = 10


@click.command()
def cli():
    rss_items = generate_fake_items(MAX_ITEMS_PER_SCREEN)
    selected_item_index = 0

    redraw(rss_items, selected_item_index)

    while True:
        selected_item_index = key_input.navigate(
            selected_item_index, MAX_ITEMS_PER_SCREEN)
        redraw(rss_items, selected_item_index)


def generate_fake_items(count):
    source = "google.com"
    date = "12/04/2020"
    return [RssItem(source, date, f"Item {item}") for item in range(1, count + 1)]


def redraw(rss_items, selected_item_index):
    click.clear()
    draw.rss_items(rss_items, rss_items[selected_item_index])


if __name__ == "__main__":
    cli()
