
def get_partner_role(user_id, cursor):


    try:
        query = """
        SELECT se.EXTENSION_KEY, se.EXTENSION_VALUE
        FROM SCI_CODE_USR_XREF cu
        JOIN SCI_ENTITY_EXTNS se ON cu.TP_OBJECT_ID = se.ENTITY_ID
        WHERE cu.USER_ID = ?
        AND se.EXTENSION_KEY IN ('DMIROUTE_WILLPRODUCE', 'DMIROUTE_WILLCONSUME')
        """

        cursor.execute(query, (user_id,))
        results = cursor.fetchall()

        # Flags for producer and consumer
        will_produce = False
        will_consume = False

        for extension_key, extension_value in results:
            val = (extension_value or '').strip().upper()
            if extension_key == 'DMIROUTE_WILLPRODUCE':
                will_produce = (val == 'TRUE')
            elif extension_key == 'DMIROUTE_WILLCONSUME':
                will_consume = (val == 'TRUE')

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
