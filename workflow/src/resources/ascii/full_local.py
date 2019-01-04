from ..assets.color import bold
from ...classes.static.join import merge
from ..ascii.forms.containers import DATABASE

localhost = bold()('''            +----------3306-----------8080---------3000--------------------------------------------------------------------------------------+
            |           {unicode}              |            |                                                                                        |
            |           |           +------+     +------+                                                                                    |
            |           +-----------|  WS  |-----|  UI  |             localhost                                                              |
            |                       +------+     +------+                                                                                    |
            |                                                                                                                                |
            +--------------------------------------------------------------------------------------------------------------------------------+
''').format(unicode = '\u25b2')

FULL_LOCAL = bold()('''

{database}
                        |
                        |
                        |
{localhost}
''').format(unicode = '\u25b2', database = merge(DATABASE), localhost = localhost)
