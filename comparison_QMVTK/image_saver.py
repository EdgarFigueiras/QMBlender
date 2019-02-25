import vtk
import os
import datetime

#Image saving function
def save_image(renderer, step):
    #Camera set Up
    renderer.GetActiveCamera().SetPosition(-105, 95, 110)
    renderer.GetActiveCamera().SetFocalPoint(0, 0, 0)
    renderer.GetActiveCamera().SetViewUp(0, 0, 1)

    renderLarge = vtk.vtkRenderLargeImage()
    renderLarge.SetInput(renderer)
    #Size of the output image, will change the brightness due to rendering issues
    renderLarge.SetMagnification(1)
    writer = vtk.vtkPNGWriter()
    writer.SetInputConnection(renderLarge.GetOutputPort())
    directory = "./rendered_images/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    writer.SetFileName("./rendered_images/" + str(step) + ".png")
    writer.Write()


#Image saving function
def save_image_camera_setup(renderer, step, camera, view):
    #Camera set Up
    renderer.GetActiveCamera().SetPosition(camera[0], camera[1], camera[2])
    renderer.GetActiveCamera().SetFocalPoint(0, 0, 0)
    renderer.GetActiveCamera().SetViewUp(view[0], view[1], view[2])
    #renderer.GetActiveCamera().SetViewUp(0, 0, 1)

    renderLarge = vtk.vtkRenderLargeImage()
    renderLarge.SetInput(renderer)
    #Size of the output image, will change the brightness due to rendering issues
    renderLarge.SetMagnification(1)
    writer = vtk.vtkPNGWriter()
    writer.SetInputConnection(renderLarge.GetOutputPort())
    directory = "./rendered_images/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    writer.SetFileName("./rendered_images/" + str(step) + ".png")
    writer.Write()

#Object saving function
def export_image(renderer, step):
    dir = "./rendered_objects/"
    if not os.path.exists(dir):
        os.makedirs(dir)
    renWin = vtk.vtkRenderWindow()

    exporter = vtk.vtkX3DExporter()
    exporter.SetFileName("testX3DExporter.x3d")
    exporter.SetInput(renWin)
    exporter.Update()
    exporter.Write()





