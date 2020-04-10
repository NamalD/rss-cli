SELECTED_ITEM_COLOUR = "\033[47;30m"
DEFAULT_COLOUR = "\033[m"


def draw_rss_items(rss_items, selected_item):
    for rss_item in rss_items:
        if rss_item == selected_item:
            draw_selected_item(rss_item)
        else:
            draw_unselected_item(rss_item)


def draw_selected_item(rss_item):
    item_formatting = format_rss_item(rss_item)
    print(SELECTED_ITEM_COLOUR + item_formatting + DEFAULT_COLOUR)


def draw_unselected_item(rss_item):
    item_formatting = format_rss_item(rss_item)
    print(item_formatting)


def format_rss_item(rss_item):
    return f"{rss_item.source} - {rss_item.date} - {rss_item.title}"
