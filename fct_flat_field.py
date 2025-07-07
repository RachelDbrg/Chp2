def flatten_fields(*fields):
    import numpy as np
    return np.concatenate([f.flatten() for f in fields])

def unflatten_fields(y, Nx, Ny, num_fields):
    import numpy as np
    total_cells = Nx * Ny
    fields = []
    for i in range(num_fields):
        start = i * total_cells
        end = (i + 1) * total_cells
        fields.append(y[start:end].reshape((Nx, Ny)))
    return fields
