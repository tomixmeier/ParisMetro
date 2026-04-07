import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import geopandas as gpd
from shapely.geometry import Point
from functions.spatial import create_buffers


def test_create_buffers():
    """Test if create_buffers generates valid buffer geometries."""
    gdf = gpd.GeoDataFrame(geometry=[Point(0, 0)], crs="EPSG:2154")
    result = create_buffers(gdf, 100)
    assert len(result) == 1
    assert result.geometry.iloc[0].area > 0