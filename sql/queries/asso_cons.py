from sql.db_adapter import execute_query

def get_associated_consumers(user_id, protocol_name, conn):
   
    query = """
    SELECT DISTINCT ci.RECEIVER_ID
    FROM CODELIST_XREF_ITEM ci
    LEFT JOIN CODELIST_XREF_VERS cv
        ON ci.LIST_NAME = cv.LIST_NAME
       AND ci.LIST_VERSION = cv.DEFAULT_VERSION
    WHERE ci.SENDER_ID = ?
      AND ci.LIST_NAME = ?
    """

    results = execute_query(conn, query, (user_id, protocol_name))

    consumers = [row['RECEIVER_ID'] for row in results if row.get('RECEIVER_ID')]
    return consumers
