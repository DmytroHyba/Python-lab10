class Camera:

    number_of_camera = 0

    def __init__(self,
                 name="pro1",
                 memory_capasity=300,
                 multiplicity_of_zoom=4,
                 producer="Poland",
                 color="ping",
                 price=250):
        self._name = name
        self._memory_capasity = memory_capasity
        self._multiplicity_of_zoom = multiplicity_of_zoom
        self._producer = producer
        self._color = color
        self._price = price

    def __del__(self):
        print('Camera {} was deleted'.format(self._name))

    def __str__(self):
        return ('name = {},   memory_capasity = {}gb,   multiplicity_of_zoom = {}x,   producer = {},   color = {},  ' +
                'price = {}$ ').format(self._name, self._memory_capasity, self._multiplicity_of_zoom,
                                         self._producer, self._color, self._price)

    @staticmethod
    def get_number_of_camera():
        return Camera.number_of_camera