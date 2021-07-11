# from rt_visualiezr import read_cam_txt
from rt_visualizer import read_cam_txt
import numpy as np
import open3d as o3d
import os


def create_cam(RT=np.eye(4), size_multiplier=1):
    camera_cone = o3d.geometry.TriangleMesh()
    camera_cone = camera_cone.create_arrow(cylinder_radius=1.0 * size_multiplier,
                                           cone_radius=1.5 * size_multiplier,
                                           cylinder_height=5.0 * size_multiplier,
                                           cone_height=4.0 * size_multiplier,
                                           resolution=10,
                                           cylinder_split=4,
                                           cone_split=1)
    camera_cone = camera_cone.paint_uniform_color(
        [np.random.rand(), np.random.rand(), np.random.rand()])

    camera_cone.transform(np.linalg.inv(RT))
    return camera_cone


def visualize_cams_rt(cam_dir, mesh_path, out_mesh_path, size_multiplier=5):
    mesh_with_cameras = o3d.geometry.TriangleMesh()

    cam_files = os.listdir(cam_dir)
    for cam_file_name in cam_files:
        if cam_file_name.endswith("cam"):
            cam_path = os.path.join(cam_dir, cam_file_name)
            cam_rt = read_cam_txt(cam_path)
            cam3d = create_cam(cam_rt, size_multiplier)

            mesh_with_cameras += cam3d

    mesh = o3d.io.read_triangle_mesh(mesh_path)

    o3d.io.write_triangle_mesh(out_mesh_path, mesh_with_cameras + mesh)
