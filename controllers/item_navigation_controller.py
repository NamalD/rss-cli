from input import keys
from input.keyboard import KeyEventHandler


class ItemNavigationController():
    __ITEM_UP = -1
    __ITEM_DOWN = +1
    __DEFAULT_INDEX = 0

    def __init__(self, on_selected_item_changed, max_items):
        self.on_selected_item_changed = on_selected_item_changed
        self.key_event_handler = self.__register_key_events()
        self.max_items = max_items

        self.current_item_index = self.__DEFAULT_INDEX
        self.on_selected_item_changed(self.__DEFAULT_INDEX)

    def activate(self):
        self.key_event_handler.handle_events()

    def __register_key_events(self):
        key_event_handler = KeyEventHandler()
        key_event_handler.handle_key(keys.UP_ARROW_KEY, self.__navigate_up)
        key_event_handler.handle_key(keys.DOWN_ARROW_KEY, self.__navigate_down)
        return key_event_handler

    def __navigate_up(self):
        self.__update_selected_item(self.__ITEM_UP)

    def __navigate_down(self):
        self.__update_selected_item(self.__ITEM_DOWN)

    def __update_selected_item(self, displacement):
        self.current_item_index = self.__wrap_index_change(displacement)
        self.on_selected_item_changed(self.current_item_index)

    def __wrap_index_change(self, displacement):
        return (
            self.current_item_index + displacement
        ) % self.max_items
