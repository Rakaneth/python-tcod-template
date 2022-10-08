import tcod

from typing import Optional
from screen import Screen, HandleResult
from tiles import TILE_WALL, TILE_FLOOR

class TestScreen(Screen):
    """A test screen."""

    def __init__(self):
        super().__init__("test")

class WinScreen(Screen):
    """You win!"""

    def __init__(self):
        super().__init__("win")
    
    def on_key(self, sym: tcod.event.KeySym) -> Optional[HandleResult]:
        return (None, False, None)

class LoseScreen(Screen):
    """You lose :("""

    def __init__(self):
        super().__init__("lose")
    
    def on_key(self, sym: tcod.event.KeySym) -> Optional[HandleResult]:
        return (None, False, None)

class PlayScreen(Screen):
    """Let's play!"""

    def __init__(self):
        super().__init__("play")
    
    def render(self, root_con: tcod.Console):
        root_con.print(0, 0, "Press [w] to win and [l] to lose")
        root_con.rgb[1, 1] = TILE_WALL["dark"]
        root_con.rgb[1, 2] = TILE_FLOOR["dark"]
    
    def on_key(self, sym: tcod.event.KeySym) -> Optional[HandleResult]:
        new_screen = None
        match sym:
            case tcod.event.K_w:
                new_screen = "win"
            case tcod.event.K_l:
                new_screen = "lose"
        
        return (new_screen, True, None)
            


        