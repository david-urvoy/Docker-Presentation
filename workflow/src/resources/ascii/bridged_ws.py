from ..assets.color import bold
from ...classes.static.join import merge
from ..ascii.forms.containers import DATABASE, WS
from ..ascii.forms.network import BRIDGE

localhost = bold()('''            +--------------------------------------------------------------------------------------------------------------------------------+
            |                                                                                                                                |
            |                                                                                                                                |
            |                                                         localhost                                                              |
            |                                                                                                                                |
            |                                                                                                                                |
            +--------------------------------------------------------------------------------------------------------------------------------+
''').format(unicode = '\u25b2')

BRIDGED_WS = bold()('''

{containers}
                        |                                      |
                        |                                      |
                        |                                      |
{network}

{localhost}
''').format(unicode = '\u25b2', containers = merge(DATABASE, WS), localhost = localhost, network = merge(BRIDGE))
