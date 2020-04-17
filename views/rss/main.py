import click
from views.rss.item import SelectedRssItemView, RssItemView


class RssView():
    def __init__(self, rss_items, selected_item):
        self.rss_items = rss_items
        self.selected_item = selected_item

        self.__draw()

    def __draw(self):
        click.clear()
        self.__draw_rss_items()

    def __draw_rss_items(self):
        for rss_item in self.rss_items:
            if rss_item == self.selected_item:
                SelectedRssItemView(rss_item)
            else:
                RssItemView(rss_item)
