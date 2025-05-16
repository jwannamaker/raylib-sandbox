import pyray as pr
from pyray import Vector3

pr.init_window(900, 900, "Raylib Experiment - OBJ Model Loading")

camera = pr.Camera3D()
camera.position = Vector3(10.0, 10.0, 10.0)
camera.target = Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = pr.CameraProjection.CAMERA_PERSPECTIVE

model_file = "resources/pentagonal_bipyramid.obj"
model_position = Vector3(0.0, 0.0, 0.0)
model = pr.load_model(model_file)

pr.disable_cursor()
pr.set_target_fps(60)

def draw_tetrahedron():
    # Brute force method for model generation
    a = Vector3(0.0, 0.0, 1.73)
    b = Vector3(1.63, 0.0, -0.58)
    c = Vector3(-0.82, 1.41, -0.58)
    d = Vector3(-0.82, -1.41, -0.58)

    pr.draw_line_3d(a, b, pr.PURPLE)
    pr.draw_line_3d(b, c, pr.PURPLE)
    pr.draw_line_3d(c, a, pr.PURPLE)

    pr.draw_line_3d(a, c, pr.PURPLE)
    pr.draw_line_3d(c, d, pr.PURPLE)
    pr.draw_line_3d(d, a, pr.PURPLE)

    pr.draw_line_3d(a, d, pr.PURPLE)
    pr.draw_line_3d(d, b, pr.PURPLE)
    pr.draw_line_3d(b, a, pr.PURPLE)

    pr.draw_line_3d(b, d, pr.PURPLE)
    pr.draw_line_3d(d, c, pr.PURPLE)
    pr.draw_line_3d(c, b, pr.PURPLE)

while not pr.window_should_close():
    pr.update_camera(camera, pr.CameraMode.CAMERA_FREE)
    pr.clear_background(pr.BLACK)

    pr.begin_drawing()
    pr.begin_mode_3d(camera)
    pr.draw_model(model, model_position, 1.0, pr.WHITE)
    # draw_tetrahedron()
    pr.draw_grid(20, 1.0)
    pr.end_mode_3d()
    pr.end_drawing()

pr.unload_model(model)
pr.close_window()
