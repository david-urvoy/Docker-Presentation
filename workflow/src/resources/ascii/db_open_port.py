from ..assets.color import bold
from ...classes.static.join import merge
from ..ascii.forms.containers import DATABASE

localhost = bold()('''            +----------3306-----------8080---------------------------------------------------------------------------------------------------+
            |           {unicode}              |                                                                                                     |
            |           |           +------+                                                                                                 |
            |           +-----------|  WS  |                          localhost                                                              |
            |                       +------+                                                                                                 |
            |                                                                                                                                |
            +--------------------------------------------------------------------------------------------------------------------------------+
''').format(unicode = '\u25b2')

DB_OPEN_PORT = bold()('''

{database}
                        |
                        |
                        |
{localhost}
''').format(unicode = '\u25b2', database = merge(DATABASE), localhost = localhost)
