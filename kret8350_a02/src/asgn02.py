def publications(conn, title=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = publications(conn)
    Use: rows = publications(conn, title=v1)
    Use: rows = publications(conn, pub_type_id=v2)
    Use: rows = publications(conn, title=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        title - a partial title (str)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
                name, the title of a publication, and the full publication
                type (i.e. 'article' rather than 'a';
        the entire table if title and pub_type_id are None,
        else rows matching the partial title and pub_type_id 
        if given 
                sorted by last name, first name, title (list of ?)
    -------------------------------------------------------
    """
    #cursor = conn.get_cursor()
    if not title and not pub_type_id:
        sql = """SELECT last_name, first_name, p_title, pt_desc
        FROM member as m INNER
        JOIN pub as p
        ON m.member_id = p.member_id 
        INNER Join pub_type as pt ON 
        pt.pub_type_id = p.pub_type_id
        ORDER BY last_name, first_name, p_title"""
        params = ()

    elif not pub_type_id and title:
        sql = """SELECT last_name, first_name, p_title
        FROM member as m INNER
        JOIN pub as p
        ON m.member_id = p.member_id 
        WHERE p_title LIKE %s
        ORDER BY last_name, first_name, p_title"""
        params = ("%" + title + "%",)

    elif pub_type_id and not title:
        sql = """SELECT last_name, first_name, p_title, pt_desc 
        FROM member as m INNER
        JOIN pub as p
        ON m.member_id = p.member_id 
        INNER Join pub_type as pt ON 
        pt.pub_type_id = p.pub_type_id
        WHERE pt.pub_type_id = %s
        ORDER BY last_name, first_name, p_title"""
        params = (pub_type_id,)

    else:
        sql = """SELECT last_name, first_name, p_title, pt_desc
        FROM member as m INNER
        JOIN pub as p
        ON m.member_id = p.member_id 
        INNER Join pub_type as pt ON 
        pt.pub_type_id = p.pub_type_id
        WHERE pt.pub_type_id = %s AND p_title LIKE  %s
        ORDER BY last_name, first_name, p_title"""
        params = (pub_type_id, "%" + title + "%")

    conn.cursor.execute(sql, params)
    rows = conn.cursor.fetchall()
    #cursor.close()
    return rows
    
    
def pub_counts(conn, member_id, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = pub_counts(conn, member_id=v1)
    Use: rows = pub_counts(conn, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of publications of type pub_type
        if given, if not, the number of all their publications (list of ?)
    -------------------------------------------------------
    """
    #cursor = conn.get_cursor()
    if member_id and pub_type_id:
        sql = """SELECT m.last_name ,m.first_name, pt.pt_desc,
        COUNT(pt.pub_type_id) 
        FROM pub AS p
        INNER JOIN member AS m 
        ON m.member_id = p.member_id
        INNER JOIN pub_type AS pt
        ON pt.pub_type_id = p.pub_type_id
        WHERE p.member_id = %s AND p.pub_type_id = %s
        """
        params = (member_id, pub_type_id)

    elif member_id and not pub_type_id:
        sql = """SELECT m.last_name ,m.first_name, pt.pt_desc,
        COUNT(pt.pub_type_id) 
        FROM pub AS p
        INNER JOIN member AS m 
        ON m.member_id = p.member_id
        INNER JOIN pub_type AS pt
        ON pt.pub_type_id = p.pub_type_id
        WHERE p.member_id = %s 
        """
        params = (member_id,)

    conn.cursor.execute(sql, params)
    rows = conn.cursor.fetchall()
    #cursor.close()
    return rows
    
    
    
def member_expertise_count(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = member_expertise_count(conn)
    Use: rows = member_expertise_count(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the count of the number of expertises they
            hold (i.e. keywords)
        all records member_id is None, sorted by last name, first name
        (list of ?)
    -------------------------------------------------------
    """
    if not member_id:
        sql = """SELECT m.last_name ,m.first_name, 
            COUNT(p.keyword_id)
            FROM member_keyword AS p
            INNER JOIN member AS m 
            ON m.member_id= p.member_id
            GROUP BY first_name, last_name """
        params = ()

    else:
        sql = """SELECT m.last_name ,m.first_name, 
            
            COUNT(p.keyword_id)
            FROM member_keyword AS p
            INNER JOIN member AS m 
            ON m.member_id= p.member_id
            WHERE p.member_id = %s
            GROUP BY first_name, last_name
            """
        params = (member_id,)

    conn.cursor.execute(sql, params)
    rows = conn.cursor.fetchall()
    #cursor.close()
    return rows
    
    
    
def all_expertise(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = all_expertise(conn)
    Use: rows = all_expertise(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, a keyword description, and a supplementary keyword description
        all records if member_id is None, 
        sorted by last_name, first_name, keyword description, supplementary 
                keyword description
    -------------------------------------------------------
    """
    if member_id:
        sql = """ SELECT m.last_name, m.first_name, k.k_desc, sk.sk_desc
        From member as m
        INNER JOIN member_supp_key as msy
        ON msy.member_id = m.member_id
        INNER JOIN supp_key as sk
        ON msy.supp_key_id = sk.supp_key_id 
        INNER JOIN keyword as k
        ON k.keyword_id= sk.keyword_id
        WHERE m.member_id = %s
        GROUP BY m.last_name, m.first_name, k.k_desc, sk.sk_desc
        """
        params = (member_id,)
    else:
        sql = """SELECT m.last_name, m.first_name, k.k_desc, sk.sk_desc
        From member as m
        INNER JOIN member_supp_key as msy
        ON msy.member_id = m.member_id
        INNER JOIN supp_key as sk
        ON msy.supp_key_id = sk.supp_key_id 
        INNER JOIN keyword as k
        ON k.keyword_id= sk.keyword_id
        GROUP BY m.last_name, m.first_name, k.k_desc, sk.sk_desc
        """
        params = ()

    conn.cursor.execute(sql, params)
    rows = conn.cursor.fetchall()
    #cursor.close()
    return rows