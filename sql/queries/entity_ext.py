from db.common.db_adapter import execute_query

def get_entity_extensions(entity_id, conn):
    """
    Fetch all extension key-value pairs for a given ENTITY_ID.

    Args:
        entity_id (str): The ENTITY_ID to fetch extensions for.
        conn: DB connection object

    Returns:
        dict: Dictionary of {EXTENSION_KEY: EXTENSION_VALUE} for non-null values.
    """
    query = """
    SELECT DISTINCT EXTENSION_KEY, EXTENSION_VALUE
    FROM SCI_ENTITY_EXTNS
    WHERE ENTITY_ID = ?
    """

    results = execute_query(conn, query, (entity_id,))

    extensions = {}
    for row in results:
        key = row['EXTENSION_KEY']
        value = row['EXTENSION_VALUE']
        if key and value:  # Skip null/empty keys or values
            extensions[key] = value

    return extensions
