from pyray import *


init_window(900, 900, "Raylib Experiment - Sphere")

camera = Camera3D()
camera.position = Vector3(10.0, 10.0, 10.0)
camera.target = Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE

model_position = Vector3(0.0, 0.0, 0.0)

disable_cursor()
set_target_fps(60)

while not window_should_close():
    update_camera(camera, CAMERA_FREE)
    clear_background(BLACK)
    
    begin_drawing()
    begin_mode_3d(camera)
    draw_sphere_wires(model_position, 5.0, 20, 10, PURPLE)
    end_mode_3d()
    end_drawing()
    
close_window()