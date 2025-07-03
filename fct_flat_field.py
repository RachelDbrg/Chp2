def flatten_fields(*fields):
    import numpy as np
    return np.concatenate([f.flatten() for f in fields])

def unflatten_fields(y, Nx, Ny, num_fields):
    import numpy as np
    split = np.split(y, num_fields)
    return [s.reshape((Nx, Ny)) for s in split]
