from ..assets.color import bold
from ...classes.static.join import merge
from ..ascii.forms.containers import *

localhost = bold()('''            +-------------------------------------------------3000-----------------------------------------------------------4000-----------------------------------------------------------5000------+
            |                                                                                                                                                                                         |
            |                                                                                                                                                                                         |
            |                                                                                  localhost                                                                                              |
            |                                                                                                                                                                                         |
            |                                                                                                                                                                                         |
            +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
''').format(unicode = '\u25b2')

MULTI_INSTANCES = bold()('''

{containers}
                      |                    |                    |                    |                    |                    |                    |                    |                    |
{network}
                                                                |                                                              |                                                              |
{localhost}
''').format(unicode = '\u25b2', containers = merge(BLUE_DATABASE, BLUE_WS, BLUE_UI, RED_DATABASE, RED_WS, RED_UI, GREEN_DATABASE, GREEN_WS, GREEN_UI), localhost = localhost, network = merge(BLUE_NETWORK, RED_NETWORK, GREEN_NETWORK))
