from pyray import *

import math

print("Hello, world!")

init_window(800, 600, "Model Showcaser")

textSize = 20

loadedModel: Model = load_model("resources/Susan.obj")
modelPosition = Vector3(0, 0, 0)
camera: Camera3D = Camera3D(Vector3(50.0, 59.0, 50.0), Vector3(0, 10, 0), Vector3(0, 1, 0), 45.0, CameraProjection.CAMERA_PERSPECTIVE)
shader: Shader = load_shader(f"resources/shaders/SimpleVertex.glsl", f"resources/shaders/SimpleColor.glsl")

loadedModel.materials[0].shader = shader
#loadedModel.materials[0]

while not window_should_close():
    update_camera(camera, CameraMode.CAMERA_ORBITAL)

    begin_drawing()

    mousePos = get_mouse_position()


    if (is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT)) :
        textSize += 1
    elif(is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT)) :
        textSize -= 1
        if(textSize < 0):
            textSize = 0


    clear_background(WHITE)
    begin_mode_3d(camera)

    
    draw_grid(20, 10)

    draw_model(loadedModel, modelPosition, 10.0, GREEN)

    end_mode_3d()
    draw_text("3D model loader", 5, 5, 30, RED)
    #draw_text("Testio", math.floor(mousePos.x), math.floor(mousePos.y), textSize, RED)

    

    end_drawing()

close_window()