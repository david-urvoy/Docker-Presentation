from ...assets.color import blue, yellow, pink, red, green, bold
from ....classes.static.join import container

DATABASE = container(pink(bold()), '''
            +-------------------------+
            |                         |
            |                         |
            |        DATABASE         |
            |                         |
            |                         |
            +----------3306-----------+''')

WS = container(blue(bold()), '''
            +-------------------------+
            |                         |
            |                         |
            |           WS            |
            |                         |
            |                         |
            +----------8080-----------+''')

UI = container(yellow(bold()), '''
            +-------------------------+
            |                         |
            |                         |
            |           UI            |
            |                         |
            |                         |
            +----------3000-----------+''')


BLUE_DATABASE = container(blue(bold()), '''
              +--------------+
              |              |
              |              |
              |   DATABASE   |
              |              |
              |              |
              +-----3306-----+''')

BLUE_WS = container(blue(bold()), '''
     +--------------+
     |              |
     |              |
     |      WS      |
     |              |
     |              |
     +-----8080-----+''')

BLUE_UI = container(blue(bold()), '''
     +--------------+
     |              |
     |              |
     |      UI      |
     |              |
     |              |
     +-----3000-----+''')

BLUE_NETWORK = container((blue(bold())), '''            +-------3306-----------------8080-----------------3000-------+
            |                                                   |        |
            |                        BLUE-NETWORK               |        |
            |                                                   |        |
            +---------------------------------------------------|--------+''')


RED_DATABASE = container(red(bold()), '''
     +--------------+
     |              |
     |              |
     |   DATABASE   |
     |              |
     |              |
     +-----3306-----+''')

RED_WS = container(red(bold()), '''
     +--------------+
     |              |
     |              |
     |      WS      |
     |              |
     |              |
     +-----8080-----+''')

RED_UI = container(red(bold()), '''
     +--------------+
     |              |
     |              |
     |      UI      |
     |              |
     |              |
     +-----3000-----+''')

RED_NETWORK = container((red(bold())), ''' +-------3306-----------------8080-----------------3000------+
 |                                                   |       |
 |                        RED-NETWORK                |       |
 |                                                   |       |
 +---------------------------------------------------|-------+''')


GREEN_DATABASE = container(green(bold()), '''
     +--------------+
     |              |
     |              |
     |   DATABASE   |
     |              |
     |              |
     +-----3306-----+''')

GREEN_WS = container(green(bold()), '''
     +--------------+
     |              |
     |              |
     |      WS      |
     |              |
     |              |
     +-----8080-----+''')

GREEN_UI = container(green(bold()), '''
     +--------------+
     |              |
     |              |
     |      UI      |
     |              |
     |              |
     +-----3000-----+''')

GREEN_NETWORK = container((green(bold())), ''' +--------3306-----------------8080-----------------3000------+
 |                                                    |       |
 |                     GREEN-NETWORK                  |       |
 |                                                    |       |
 +----------------------------------------------------|-------+''')
