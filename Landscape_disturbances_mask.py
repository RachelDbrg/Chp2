def create_barrier_mask(shape, orientation='vertical', thickness=1, position='center'):

    import numpy as np

    
    """
    Creates a binary mask with an impassable barrier.

    Parameters:
        shape (tuple): (Nx, Ny) shape of the landscape
        orientation (str): 'vertical' or 'horizontal'
        thickness (int): number of grid cells wide the barrier is
        position (str or int): 'center', 'left', 'right' (or custom index)

    Returns:
        mask (ndarray): boolean array with True where barrier exists
    """
    Nx, Ny = shape
    mask = np.zeros(shape, dtype=bool)

    if orientation == 'vertical':
        if position == 'center':
            idx = Ny // 2
        elif position == 'left':
            idx = Ny // 4
        elif position == 'right':
            idx = 3 * Ny // 4
        else:
            idx = int(position)
        mask[:, idx:idx+thickness] = True

    elif orientation == 'horizontal':
        if position == 'center':
            idx = Nx // 2
        elif position == 'top':
            idx = Nx // 4
        elif position == 'bottom':
            idx = 3 * Nx // 4
        else:
            idx = int(position)
        mask[idx:idx+thickness, :] = True

    return mask
