import click
from models.rss import RssItem
from view.draw import draw_rss_items


def generate_items(count):
    source = "google.com"
    date = "12/04/2020"
    return [RssItem(source, date, f"Item {item}") for item in range(1, count + 1)]


@click.command()
def cli():
    rss_items = generate_items(10)
    selected_item = rss_items[0]
    draw_rss_items(rss_items, selected_item)


if __name__ == "__main__":
    cli()
