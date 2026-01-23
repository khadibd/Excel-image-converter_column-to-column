def validate(results, min_kb=200, max_kb=300):
    errors = []
    for r in results:
        if r.size_kb < min_kb or r.size_kb > max_kb:
            errors.append(r.row)
    return errors
