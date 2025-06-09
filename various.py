import magpylib as magpy
import numpy as np

# Reset defaults set in previous example
magpy.defaults.reset()

# Define sensor with path
sensor = magpy.Sensor(pixel=[(0, 0, -0.0005), (0, 0, 0.0005)], style_size=1.5)
sensor.position = np.linspace((0, 0, -0.003), (0, 0, 0.003), 37)

angles = np.linspace(0, 360, 37)
sensor.rotate_from_angax(angles, "z", start=0)

# Define source with path
cyl1 = magpy.magnet.Cylinder(
    polarization=(0.1, 0, 0), dimension=(0.001, 0.002), position=(0.003, 0, 0)
)
cyl1.rotate_from_angax(-angles, "z", start=0)

# Display system and field at sensor
with magpy.show_context(sensor, cyl1, animation=True, backend="plotly"):
    magpy.show(col=1)
    magpy.show(output="Bx", col=2, pixel_agg=None)
