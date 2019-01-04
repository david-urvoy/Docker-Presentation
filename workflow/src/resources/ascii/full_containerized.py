from ..assets.color import bold
from ...classes.static.join import merge
from ..ascii.forms.containers import DATABASE, WS, UI
from ..ascii.forms.network import USER_NETWORK

localhost = bold()('''            +-------------------------------------------------8080-----------------------------------3000------------------------------------+
            |                                                                                                                                |
            |                                                                                                                                |
            |                                                         localhost                                                              |
            |                                                                                                                                |
            |                                                                                                                                |
            +--------------------------------------------------------------------------------------------------------------------------------+
''').format(unicode = '\u25b2')

FULL_CONTAINERIZED = bold()('''

{containers}
                        |                                      |                                      |
                        |                                      |                                      |
                        |                                      |                                      |
{network}
                                                               |                                      |
{localhost}
''').format(unicode = '\u25b2', containers = merge(DATABASE, WS, UI), localhost = localhost, network = merge(USER_NETWORK))
