from shapely.geometry import Point
from patterns.geometry import Geometry


def test_geometry_defaults():
    geom = Geometry(Point(142, -37))

    assert "POINT (142 -37)" in geom.to_graph().serialize()


def test_geometry_geojson():
    geom = Geometry(Point(142, -37), serialization_type="geojson")

    assert "[142.0,-37.0]" in geom.to_graph().serialize()