def add_rule(p: dict, key, rule):
    if key in p and rule not in p[key]:
        p[key].append(rule)
    else:
        p[key] = list()
        p[key].append(rule)