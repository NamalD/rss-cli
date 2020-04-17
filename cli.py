import click
from models.rss import RssItem
from controllers.rss_items_controller import RssItemController


MAX_ITEMS_PER_SCREEN = 10


@click.command()
def cli():
    fake_rss_items = generate_fake_items(MAX_ITEMS_PER_SCREEN)

    rss_item_controller = RssItemController(
        fake_rss_items,
        MAX_ITEMS_PER_SCREEN)

    rss_item_controller.activate()


def generate_fake_items(count):
    source = "google.com"
    date = "12/04/2020"
    return [RssItem(source, date, f"Item {item}") for item in range(1, count + 1)]


if __name__ == "__main__":
    cli()
