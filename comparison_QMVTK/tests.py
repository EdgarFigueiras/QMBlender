import vtkpoints as vtkp

#Cav    100
#Vort   57
#Gauss  30
#DarkM  100¿?

#vtkp.render_simulation("vortex_barrier30k.3d", 30000, 0, 200, 0, 0.05, 3000, 2, 50, 1)

#vtkp.render_simulation_images_multiprocess("vortex_barrier50k.3d", 50000, 0, 200, 0, 0.05, 2, 50, -105, 95, 110,  1)

#vtkp.render_simulation("soliton_barrera50k.3d", 30000, 190, 200, 0, 0.05, 3000, 2, 100, 1)

#vtkp.render_simulation_images_multiprocess("soliton_barrera50k.3d", 50000, 0, 200, 0, 0.05, 2, 50, -105, 95, 110,  1)





#darkmat.3d [62, -168, 88], [0.5146, -0.2401, -0.8230], last_step = 249, cube_size = 60, particles_size = 2, max_Psi = 100000

#Cav3dData.3d [-226, 114, -239], [0.2325, 0.9552, 0.1827], last_step = 100, cube_size = 100, particles_size = 3, max_Psi = 0.05

#Vort3dData.3d [-102, -217, 117], [0.2356, 0.3719, 0.8978], last_step = 57, cube_size = 80, particles_size = 2, max_Psi = 1

#vortex_barrier30kV2.3d [-105, 95, 110], [0, 0, 1], last_step = 200, cube_size = 50,  particles_size = 2, max_Psi = 0.025

#soliton_barrera50k.3d [-227, 130, -180], [0.210064, 0.9538159, 0.214727], last_step = 200, cube_size = 80, particles_size = 2, max_Psi = 0.05


path = "darkmat.3d"
n_particles = 50000
first_step = 0
last_step = 249
min_Psi = 0
max_Psi = 100000
particles_size = 2
cube_size = 60
camera = [62, -168, 88]
view = [0.5146, -0.2401, -0.8230]
info = 1
time_step = 3000

#vtkp.render_simulation_images_multiprocess(path, n_particles, first_step, last_step, min_Psi, max_Psi, particles_size, cube_size, camera, view, info)

vtkp.render_simulation(path, n_particles, first_step, last_step, min_Psi, max_Psi, time_step, particles_size, cube_size, info)







