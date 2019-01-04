from ..assets.color import red, bold
from ...classes.static.join import merge
from ..ascii.forms.containers import DATABASE

cross = "X"

localhost = bold()('''            +----------3306-----------8080---------------------------------------------------------------------------------------------------+
            |           {unicode}              |                                                                                                     |
            |           |           +------+                                                                                                 |
            |           +-----------|  WS  |                          localhost                                                              |
            |                       +------+                                                                                                 |
            |                                                                                                                                |
            +--------------------------------------------------------------------------------------------------------------------------------+
''').format(unicode = '\u25b2')

DB_CLOSED_PORT = bold()('''

{database}
                        |
                        {cross}
                        |
{localhost}
''').format(unicode = '\u25b2', database = merge(DATABASE), localhost = localhost, cross = red()(cross))
