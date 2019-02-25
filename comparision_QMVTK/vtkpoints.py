import vtk
import numpy as np
import random
import math
import time as tm
import multiprocessing
from multiprocessing import Process
import actor_manage as actor_man
import image_saver as img_save
from step_timer import vtkTimerCallback

bg_color = 255

#Renders the simulation of the file passed
# path -> File path of the numpy array with the 3d data
# n_particles -> number of particles that will be rendered in the simulation each step
# first_step -> starting step of the simulation
# last_step -> ending step of the simulation
# min_Psi -> minimum Psi value to represent the colors of the simulation
# max_Psi -> maximum Psi value to represent the colors of the simulation
# time_step -> time elapsed between steps, measured in miliseconds
# info -> flag, 1==Print info, 0==Dont show info
def render_simulation(path, n_particles, first_step, last_step, min_Psi, max_Psi, time_step, particles_size, cube_size, info):
    if (info>0):
        print("path: ", path , "\n", "first step: ", first_step, "  last step: ", last_step)
        print(" min_Psi: ", min_Psi, "  max_Psi: ", max_Psi, "  time_step: ", time_step, "ms")
    
    actor = actor_man.create_actor(path, n_particles, first_step, min_Psi, max_Psi, particles_size)

    renderer = vtk.vtkOpenGLRenderer()
    renderer.SetBackground(bg_color,bg_color,bg_color)
    renderer.AddViewProp(actor)

    cubeActor = actor_man.create_cube_actor(cube_size)
    renderer.AddViewProp(cubeActor)
    cubeAxes = actor_man.cube_axes(cube_size)
    renderer.AddViewProp(cubeAxes)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(1600,1200)
    renderWindow.AddRenderer(renderer)

    renWinInteractor = vtk.vtkRenderWindowInteractor()
    renWinInteractor.SetRenderWindow(renderWindow)
    renWinInteractor.Render()
    
    print("Steps:")
    print(first_step)

    
    # Initialize must be called prior to creating timer events.
    renWinInteractor.Initialize()
        
    # Sign up to receive TimerEvent
    timerCallback = vtkTimerCallback(path, n_particles, first_step + 1, last_step, min_Psi, max_Psi, particles_size, cube_size, info)
    timerCallback.actor = actor
    renWinInteractor.AddObserver('TimerEvent', timerCallback.execute)
    timerId = renWinInteractor.CreateRepeatingTimer(time_step);

    renWinInteractor.Start()



#Renders the simulation of the file passed and saves it as image
# path -> File path of the numpy array with the 3d data
# n_particles -> number of particles that will be rendered in the simulation each step
# first_step -> starting step of the simulation
# last_step -> ending step of the simulation
# min_Psi -> minimum Psi value to represent the colors of the simulation
# max_Psi -> maximum Psi value to represent the colors of the simulation
# info -> flag, 1==Print info, 0==Dont show info
# process_number -> Id of the process executing this function
def render_simulation_for_multiprocess(path, n_particles, first_step, last_step, min_Psi, max_Psi, particles_size, cube_size, camera, view, info, process_number):
    
    #start_time = tm.time()
   
    #if (info>0):
    #    print("path: ", path , "\n", "first step: ", first_step, "  last step: ", last_step)
    #    print(" min_Psi: ", min_Psi, "  max_Psi: ", max_Psi, "  time_step: ", time_step, "ms")
    
    total_steps = last_step - first_step + 1
    
    renderer = vtk.vtkOpenGLRenderer()
    renderer.SetBackground(bg_color,bg_color,bg_color)
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(2048,1536)
    #Disables the 3D render window
    renderWindow.SetOffScreenRendering(1);
    renWinInteractor = vtk.vtkRenderWindowInteractor()

    for actual_step in range(0,total_steps):
        actor = actor_man.create_actor(path, n_particles, actual_step + first_step, min_Psi, max_Psi, particles_size)
        renderer.AddViewProp(actor)
        
        '''
        #Add cube to the render
        cubeActor = actor_man.create_cube_actor(cube_size)
        renderer.AddViewProp(cubeActor)
        cubeAxes = actor_man.cube_axes(cube_size)
        renderer.AddViewProp(cubeAxes)
        '''
        
        renderWindow.AddRenderer(renderer)

        renWinInteractor.SetRenderWindow(renderWindow)
        renWinInteractor.Render()
        renWinInteractor.Initialize()
        if (info>0):
            print("Pr:", process_number, "  Step:", actual_step + first_step  )
    
        img_save.save_image_camera_setup(renderer, actual_step + first_step, camera, view)
        #img_save.export_image(renderer, actual_step + first_step)
        renderer.RemoveAllViewProps()

    #elapsed_time = tm.time() - start_time

    #print("Time elapsed: ", elapsed_time)


#Renders the simulation of the file passed and saves it as image
# Works as a decorator to enable adapted multiprocess flow
# Calculates the number of processes that will be used and distribute
#   using an balanced algorithm with a calculation of the steps per process
# path -> File path of the numpy array with the 3d data
# n_particles -> number of particles that will be rendered in the simulation each step
# first_step -> starting step of the simulation
# last_step -> ending step of the simulation
# min_Psi -> minimum Psi value to represent the colors of the simulation
# max_Psi -> maximum Psi value to represent the colors of the simulation
# info -> flag, 1==Print info, 0==Dont show info
def render_simulation_images_multiprocess(path, n_particles, first_step, last_step, min_Psi, max_Psi, particles_size, cube_size, camera, view, info):

    #print("Number of cpu : ", multiprocessing.cpu_count())
    #Calculates the number of cpus
    number_processors = multiprocessing.cpu_count()
    
    #Calculations to balance the work between process
    #Total steps of the simulation
    total_steps = last_step - first_step
    #Steps that will be done by each process
    steps_per_process = round(total_steps / number_processors)
    print("Total steps : ", total_steps)
    print("Steps per process : ", steps_per_process)
    procs = []
    start_step = first_step
    finish_step = first_step + steps_per_process
    
    #Loop that launch the process with the amount of work balanced
    for num_process in range (0,number_processors):
        if (num_process == number_processors - 1):
            finish_step = last_step
        print("Process:", num_process, " Start step:", start_step, "  finish_step:", finish_step)
        proc = Process(target=render_simulation_for_multiprocess, args=(path, n_particles, start_step, finish_step, min_Psi, max_Psi, particles_size, cube_size, camera, view, info, num_process))
        procs.append(proc)
        proc.start()
        start_step =  finish_step + 1
        finish_step = start_step + steps_per_process -1






