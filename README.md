# mvs_texturing_rt_visualization

Debugging tool to visualize camera's extrinsics for mvs texturing.

# Usage

Install requirements:
```
pip install -r requirements.txt
```

Colorful arrows will show you camera's  position and direction:
```
python visualize_cameras.py -cams_dir /your_cameras_dir -mesh /your_mesh.PLY -out_mesh /your_output_mesh.PLY
```