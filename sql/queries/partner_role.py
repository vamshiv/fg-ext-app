import ibm_db

def get_partner_role(user_id, conn):
    
    try:
        query = """
        SELECT se.EXTENSION_KEY, se.EXTENSION_VALUE
        FROM SCI_CODE_USR_XREF cu
        JOIN SCI_ENTITY_EXTNS se ON cu.TP_OBJECT_ID = se.ENTITY_ID
        WHERE cu.USER_ID = ?
        AND se.EXTENSION_KEY IN ('DMIROUTE_WILLPRODUCE', 'DMIROUTE_WILLCONSUME')
        """

        # Prepare and execute statement
        stmt = ibm_db.prepare(conn, query)
        ibm_db.execute(stmt, (user_id,))

        # Flags for producer and consumer
        will_produce = False
        will_consume = False

        row = ibm_db.fetch_assoc(stmt)
        while row:
            extension_key = row['EXTENSION_KEY']
            extension_value = (row['EXTENSION_VALUE'] or '').strip().upper()

            if extension_key == 'DMIROUTE_WILLPRODUCE':
                will_produce = (extension_value == 'TRUE')
            elif extension_key == 'DMIROUTE_WILLCONSUME':
                will_consume = (extension_value == 'TRUE')

            row = ibm_db.fetch_assoc(stmt)

        # Determine role
        if will_produce and not will_consume:
            return 'Producer'
        elif will_consume and not will_produce:
            return 'Consumer'
        elif will_produce and will_consume:
            return 'Producer & Consumer'
        else:
            return 'Unknown'

    except Exception as e:
        print(f"[PartnerRole] Error fetching role for user {user_id}: {e}")
        return 'Unknown'
