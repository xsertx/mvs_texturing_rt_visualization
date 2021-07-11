import numpy as np


def read_cam_txt(filepath):
    RT = np.eye(4)
    with open(filepath) as f:
        extrinsics_str, intrinsics_str = f.read().split("\n")
        extrinsics = np.array([float(i) for i in extrinsics_str.split(" ")])
        T = extrinsics[:3]
        R = extrinsics[3:]

        R = R.reshape((3, 3))
        RT[:3, :3] = R
        RT[:3, 3] = T

        intrinsics = [float(i) for i in intrinsics_str.split(" ")]
    return RT
