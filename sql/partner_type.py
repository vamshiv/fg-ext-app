from sql.queries.partner_role import get_partner_role

def determine_partner_type(user_id, cursor):
    
    print(f"[UserType] Determining user type for USER_ID: {user_id}")
    return get_partner_role(user_id, cursor)
