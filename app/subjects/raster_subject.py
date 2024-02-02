# app/subjects/raster_subject.py
from observer.subject import Subject
from utils.log_handler import LogHandler
import rasterio
from rasterio.plot import reshape_as_image

class RasterSubject(Subject):
    def __init__(self, file_path):
        super().__init__()
        self._raster_path = file_path
        self._state = self._load_raster_data()  # State representing raster data

    def _load_raster_data(self):
        """Load raster data from the file."""
        with rasterio.open(self._raster_path) as src:
            return reshape_as_image(src.read())

    def get_state(self):
        """Get the current state of the raster subject."""
        return self._state

    def set_state(self, state):
        """Set the state of the raster subject."""
        self._state = state
        self.notify()  # Notify observers when the state changes

    def get_raster_path(self):
        """Get the path of the raster file."""
        return self._raster_path