import click
from views.drawing import colour


class RssItemView():
    def __init__(self, rss_item):
        self.rss_item = rss_item

        formatted_item = self.__format_rss_item(self.rss_item)
        self.draw(formatted_item)

    def draw(self, formatted_item):
        click.echo(formatted_item)

    def __format_rss_item(self, rss_item):
        return f"{rss_item.source} - {rss_item.date} - {rss_item.title}"


class SelectedRssItemView(RssItemView):
    def draw(self, item_formatting):
        click.echo(colour.SELECTED_ITEM + item_formatting + colour.DEFAULT)
