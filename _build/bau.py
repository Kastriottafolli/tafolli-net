"""Compatibility entry point: builds the three homepages and automation page."""
from artwork import build as build_artwork
from experience import build

if __name__ == "__main__":
    build_artwork()
    build()
