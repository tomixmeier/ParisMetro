import geopandas as gpd


def reproject_to_metric(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Reproject GeoDataFrame to a metric CRS (EPSG:2154)."""
    return gdf.to_crs(epsg=2154)


def create_buffers(gdf: gpd.GeoDataFrame, radius: int) -> gpd.GeoDataFrame:
    """Create buffer polygons around geometries with given radius.
    Parameters: gdf (GeoDataFrame): Input data
    Returns: GeoDataFrame: Reprojected data"""
    gdf = gdf.copy()
    gdf["geometry"] = gdf.buffer(radius)
    return gdf