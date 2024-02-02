# app/subjects/raster_subject_view_pool.py
from .raster_subject_view import RasterSubjectView

class RasterSubjectViewPool:
    def __init__(self):
        self.views = []

    def open_view(self, raster_subject):
        view = RasterSubjectView(raster_subject)
        view.closed.connect(self.remove_closed_view)
        self.views.append(view)
        view.show()

    def close_all_views(self):
        for view in self.views:
            self.remove_closed_view(view)

    def remove_closed_view(self, view):
        if view in self.views:
            self.views.remove(view)   
            view.close()