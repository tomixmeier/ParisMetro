import geopandas as gpd
from rasterstats import zonal_stats


def extract_mean_raster_value(
    polygons: gpd.GeoDataFrame,
    raster_path: str,
    value_column: str = "income_mean"
) -> gpd.GeoDataFrame:
    """Extract mean raster values per polygon and add as new column.
    Parameters:
        polygons (GeoDataFrame): Input polygons
        raster_path (str): Path to raster
        value_column (str): Name of output column
    Returns: GeoDataFrame: Polygons with mean values and cell counts"""
    result = polygons.copy()

    stats = zonal_stats(
        vectors=result.geometry,
        raster=raster_path,
        stats=["mean", "count"],
        all_touched=True
    )

    result[value_column] = [s["mean"] for s in stats]
    result["n_cells"] = [s["count"] for s in stats]

    return result