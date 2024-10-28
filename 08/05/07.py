def limiter(limit, unique, lookup):
    instances = {}
    lookup = 0 if lookup == 'FIRST' else -1
    def decorator(cls):
        def create_instance(*args, **kwargs):
            _instance = cls(*args, **kwargs)
            _id = getattr(_instance, unique)
            if _id in instances:
                _instance =  instances[_id]
            else:
                if len(instances)>=limit:
                    return [v for k,v in instances.items()][lookup]
                else:
                    instances[_id] = _instance
            return _instance
        return create_instance
    return decorator