#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Make a sample animation."""

import argparse
from cairomovie import anim

class Animation(anim.Animation):
    def duration(self, config):
        return 10

    def draw_frame(self, c, t, config):
        """Draw one animation frame to the cairo context."""
        c.set_source_rgb(0,0,0)
        c.paint()
        c.set_source_rgb(1,0,0)
        c.rectangle(0, 0, config.w * t / self.duration(config), config.h)
        c.fill()

def main():
    """Parse the command line and run the script."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        fromfile_prefix_chars='@',
        description=__doc__)
    anim.add_anim_arguments(parser)
    args = parser.parse_args()

    animation = Animation()
    anim.render_from_args(animation, args)

if __name__ == '__main__':
    main()