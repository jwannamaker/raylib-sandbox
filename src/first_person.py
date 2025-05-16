from pyray import init_window, Camera3D, Vector3, CameraProjection, disable_cursor, window_should_close, CameraMode, update_camera, clear_background, set_target_fps, Color, begin_drawing, end_drawing, begin_mode_3d, end_mode_3d, draw_sphere_wires, close_window, draw_sphere

def main():
    init_window(900, 900, "Raylib Experiement")
    camera = Camera3D()
    camera.position = Vector3(10.0, 10.0, 10.0)
    camera.target = Vector3(0.0, 0.0, 0.0)
    camera.up = Vector3(0.0, 1.0, 0.0)
    camera.fovy = 45.0
    camera.projection = CameraProjection.CAMERA_PERSPECTIVE
    disable_cursor()
    set_target_fps(60)

    model_position = Vector3(0.0, 0.0, 0.0)

    while not window_should_close():
        update_camera(camera, CameraMode.CAMERA_FREE)
        clear_background(Color(0, 0, 0, 255))

        begin_drawing()
        begin_mode_3d(camera)
        draw_sphere_wires(model_position, 5.0, 20, 20, Color(100, 100, 0, 255))
        draw_sphere(model_position, 3.0, Color(0, 150, 0, 255))
        end_mode_3d()
        end_drawing()

    close_window()

if __name__ == "__main__":
    main()
