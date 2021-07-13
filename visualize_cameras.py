from rt_visualizer import visualize_cams_rt
import argparse


parser = argparse.ArgumentParser(
    description='Process inputs for camera visualization.')

parser.add_argument('-cams_dir',  type=str, help='path to cameras file')
parser.add_argument('-mesh',  type=str, help='path to mesh path')
parser.add_argument('-out_mesh',  type=str,
                    help='path to mesh with visualized cameras')

args = parser.parse_args()


def main():
    cams_dir = args.cams_dir
    mesh_path = args.mesh
    out_mesh_path = args.out_mesh

    visualize_cams_rt(cams_dir, mesh_path, out_mesh_path)


if __name__ == "__main__":
    main()
