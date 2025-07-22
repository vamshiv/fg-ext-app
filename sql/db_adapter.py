import ibm_db

def execute_query(conn, query, params=()):
   
    try:
        stmt = ibm_db.prepare(conn, query)
        ibm_db.execute(stmt, params)
        
        results = []
        row = ibm_db.fetch_assoc(stmt)
        while row:
            results.append(row)
            row = ibm_db.fetch_assoc(stmt)
        return results

    except Exception as e:
        print(f"[DBAdapter] Error executing query: {e}")
        return []
