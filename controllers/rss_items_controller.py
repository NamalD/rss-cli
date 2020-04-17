from views.rss.main import RssView
from controllers.item_navigation_controller import ItemNavigationController


class RssItemController():
    def __init__(self, rss_items, max_items):
        self.rss_items = rss_items
        self.max_items = max_items

    def activate(self):
        item_nav_controller = ItemNavigationController(
            self.__set_item_index,
            self.max_items)

        while True:
            item_nav_controller.activate()

    def __set_item_index(self, new_item_index):
        self.selected_item_index = new_item_index
        self.__view_items()

    def __view_items(self):
        RssView(self.rss_items, self.__get_selected_item())

    def __get_selected_item(self):
        return self.rss_items[self.selected_item_index]
