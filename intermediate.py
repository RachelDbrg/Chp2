# def log_intermediates(t, logged_data, **fields):
#     for name, value in fields.items():
#         try:
#             logged_value = value.copy()
#         except AttributeError:
#             logged_value = value  # fallback for scalars like floats
#         if name in logged_data:
#             logged_data[name].append((t, logged_value))
#         else:
#             logged_data[name] = [(t, logged_value)]


import os
import numpy as np

def make_disk_logger(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    def log_fn(t, **kwargs):
        filename = os.path.join(output_dir, f"log_t_{t:.2f}.npz")
        np.savez_compressed(filename, t=t, **kwargs)
    
    return log_fn


# import os
# import pickle

# def make_disk_logger(output_dir, buffer_size=10):
#     os.makedirs(output_dir, exist_ok=True)
#     buffer = []
#     counter = 0

#     def log_fn(t, fields, extras):
#         nonlocal counter
#         buffer.append((t, fields, extras))
#         if len(buffer) >= buffer_size:
#             filename = os.path.join(output_dir, f"log_{counter:05d}.pkl")
#             with open(filename, 'wb') as f:
#                 pickle.dump(buffer, f)
#             buffer.clear()
#             counter += 1

#     return log_fn