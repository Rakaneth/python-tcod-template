import tcod
import screens
import screens.screen
import screens.test

from typing import Dict, Optional
from logutil import LOGGER

class Engine:
    "Class to manage the game loop"

    def __init__(self, scr_w: int, scr_h: int):
        tileset = tcod.tileset.load_tilesheet(
            "assets/font/anikki_20x20.png", 16, 16, tcod.tileset.CHARMAP_CP437
        )
        self.console = tcod.Console(scr_w, scr_h, order='F')
        self.context = tcod.context.new(
            columns=self.console.width, rows=self.console.height, tileset=tileset
        )
        self.screens: Dict[str, screens.screen.Screen] = dict()
        self.cur_screen: Optional[screens.screen.Screen] = None
    
    def init(self):
        """Initialize game data."""
        scrs: list[screens.screen.Screen] = [
            screens.test.PlayScreen(),
            screens.test.WinScreen(),
            screens.test.LoseScreen()
        ]
        for scr in scrs:
            self.screens[scr.name] = scr
        
        self.cur_screen = self.screens["play"]

    
    def run(self):
        """Main game loop."""
        running = True
        with self.context as context:
            while running:
                self.console.clear()
                if self.cur_screen is not None:
                    self.cur_screen.render(self.console)
                    context.present(self.console)
                else:
                    LOGGER.log("ERROR", "No current screen")
                    raise SystemExit()

                for event in tcod.event.wait():
                    context.convert_event(event)
                    hr = self.cur_screen.dispatch(event)
                    if hr is not None:
                        (new_screen, running, action) = hr
                        if new_screen:
                            self.cur_screen = self.screens[new_screen]
            
        self.cur_screen.dispatch(tcod.event.Quit())
                    