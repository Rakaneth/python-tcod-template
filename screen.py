from collections import namedtuple
import tcod

from typing import Optional

HandleResult = namedtuple("HandleResult", ("new_screen", "running", "action"))

class Screen(tcod.event.EventDispatch[HandleResult]):
    """Game screens that handle input and rendering."""

    def __init__(self, name: str):
        self.name = name
    
    def render(self, root_con: tcod.Console):
        root_con.print(0, 0, f"This is the {self.name} screen.")
    
    def on_key(self, sym: tcod.event.KeySym) -> Optional[HandleResult]:
        pass

    def on_quit(self, event: tcod.event.Quit) -> Optional[HandleResult]:
        raise SystemExit()
    
    def on_click(self, x: int, y: int, btn: int) -> Optional[HandleResult]:
        pass

    def on_mouse_move(self, x: int, y: int) -> Optional[HandleResult]:
        pass

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[HandleResult]:
        return self.on_key(event.sym)
    
    def ev_quit(self, event: tcod.event.Quit) -> Optional[HandleResult]:
        return self.on_quit(event)
    
    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[HandleResult]:
        return self.on_click(event.tile.x, event.tile.y, event.button)
    
    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> Optional[HandleResult]:
        return self.on_mouse_move(event.tile.x, event.tile.y)

    

        