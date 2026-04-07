import geopandas as gpd


def load_stations(path: str) -> gpd.GeoDataFrame:
    """Load station data as GeoDataFrame.
    Parameters: path (str): Path to dataset
    Returns: GeoDataFrame: Station data"""
    return gpd.read_file(path)


def load_income_grid(path: str) -> gpd.GeoDataFrame:
    """Load income grid data as GeoDataFrame.
    Parameters: path (str): Path to dataset
    Returns: GeoDataFrame: Income grid"""
    return gpd.read_file(path)

def load_metro_lines(path: str) -> gpd.GeoDataFrame:
    """Load metro line data as GeoDataFrame.
    Parameters: path (str): Path or URL
    Returns: GeoDataFrame: Metro lines"""
    return gpd.read_file(path)
    




