# from pyray import *
import pyray as pr

pr.init_window(900, 900, "Raylib Experiment - Sphere")

camera = pr.Camera3D()
camera.position = pr.Vector3(10.0, 10.0, 10.0)
camera.target = pr.Vector3(0.0, 0.0, 0.0)
camera.up = pr.Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = pr.CameraProjection.CAMERA_PERSPECTIVE

model_position = pr.Vector3(0.0, 0.0, 0.0)

pr.disable_cursor()
pr.set_target_fps(60)

while not pr.window_should_close():
    pr.update_camera(camera, pr.CameraMode.CAMERA_FREE)
    pr.clear_background(pr.BLACK)

    pr.begin_drawing()
    pr.begin_mode_3d(camera)
    pr.draw_sphere_wires(model_position, 5.0, 20, 10, pr.PURPLE)
    pr.end_mode_3d()
    pr.end_drawing()

pr.close_window()
