def check_bounds(label, x_min, x_max, y_min, y_max, Nx, Ny):
    assert 0 <= x_min < Nx, f"{label}_x_min out of bounds"
    assert 0 <= x_max < Nx, f"{label}_x_max out of bounds"
    assert 0 <= y_min < Ny, f"{label}_y_min out of bounds"
    assert 0 <= y_max < Ny, f"{label}_y_max out of bounds"
