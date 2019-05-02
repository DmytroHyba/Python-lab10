import camera

default_camera = camera.Camera()
ordinary_camera = camera.Camera(name='pro2',
                           memory_capasity=500,
                           multiplicity_of_zoom=6,
                           producer='China',
                           color='White',
                           price=390)
professional_camera = camera.Camera(name="pro3",
                              memory_capasity=999,
                              multiplicity_of_zoom=8,
                              producer= 'USA',
                              price=510,
                              color="dark",)
print(default_camera)
print(ordinary_camera)
print(professional_camera)
