def apply_wheres(query, wheres):
    if wheres == None:
        return query

    query += ' WHERE'
    for key, value in wheres.items():
        if not query[-5:] == 'WHERE':
            query += ' AND'
        query += f' {key} = {value}'

    return query
