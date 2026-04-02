import geopandas as gpd


def load_stations(path: str) -> gpd.GeoDataFrame:
    return gpd.read_file(path)


def load_income_grid(path: str) -> gpd.GeoDataFrame:
    return gpd.read_file(path)

def load_metro_lines(path: str) -> gpd.GeoDataFrame:
    return gpd.read_file(path)
    




