import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

import geopandas as gpd
from shapely.geometry import Point
from functions.spatial import reproject_to_metric, create_buffers


def test_spatial_workflow():
    """Test if the spatial workflow runs correctly."""
    gdf = gpd.GeoDataFrame(geometry=[Point(2.35, 48.85)], crs="EPSG:4326")

    projected = reproject_to_metric(gdf)
    buffered = create_buffers(projected, 100)

    assert projected.crs.to_epsg() == 2154
    assert len(buffered) == 1
    assert buffered.geometry.iloc[0].area > 0