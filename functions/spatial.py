import geopandas as gpd


def reproject_to_metric(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    return gdf.to_crs(epsg=2154)


def create_buffers(gdf: gpd.GeoDataFrame, radius: int) -> gpd.GeoDataFrame:
    gdf = gdf.copy()
    gdf["geometry"] = gdf.buffer(radius)
    return gdf