from input_handlers.url_handler import url_handler
from input_handlers.list_handler import list_handler
from input_handlers.raw_handler import raw_handler

def loader(url, raw_request, list, cookie, mode, thread, silent, output):
    if url and not (raw_request or list):
        return url_handler(url, cookie, mode, thread, silent, output)

    elif raw_request and not (url or list):
        return raw_handler(raw_request, cookie, mode, thread, silent, output)

    elif list and not (url and raw_request):
        return list_handler(list, cookie, mode, thread, silent, output)

    else:
        raise ValueError("Only one input source must be provided: either --url or --raw_request or --list.")
