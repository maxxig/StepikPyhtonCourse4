def pluck( data, path, default = None):
    t = path.split('.')
    if len(t) == 1:
        if data.get(t[0]):
            return data.get(t[0])
        else:
            return default
    if len(t)>=2:
        return pluck(data.get(t[0]), '.'.join(t[1:]), default)