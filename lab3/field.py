# def field(items, *args):
#     assert len(args) > 0
#     if len(args) == 1:
#         for item in items:
#             for arg in args:
#                 if arg in item:
#                     yield item[arg]
#     else:
#         for item in items:
#             new_item = {}
#             for arg in args:
#                 if arg in item:
#                     new_item[arg] = item[arg]


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            for arg in args:
                if arg in item:
                    yield item[arg]
    else:
        for item in items:
            new_item = {}
            for arg in item:
                if arg in item:
                    new_item[arg] = item[arg]
            if len(new_item.keys()) > 0:
                yield new_item
