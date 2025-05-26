import sys

from . import weather_forecast


if len(sys.argv) > 1:
    print("Coordinates:", weather_forecast(sys.argv[1]))
else:
    print("Syntax")