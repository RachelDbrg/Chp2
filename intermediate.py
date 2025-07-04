def log_intermediates(t, logged_data, **fields):
    for name, value in fields.items():
        try:
            logged_value = value.copy()
        except AttributeError:
            logged_value = value  # fallback for scalars like floats
        if name in logged_data:
            logged_data[name].append((t, logged_value))
        else:
            logged_data[name] = [(t, logged_value)]
