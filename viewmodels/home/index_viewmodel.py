from spookyMap.viewmodels.shared.viewmodelbase import ViewModelBase
from spookyMap.services import map_service


class IndexViewModel(ViewModelBase):
    def __init__(self, lngW, latS, lngE, latN):
        super().__init__()
        self.description = self.request_dict.description
        self.latitude = self.request_dict.latitude
        self.longitude = self.request_dict.longitude
        self.ghosts_list = map_service.get_landmarks_from_bounds(lngW, latS, lngE, latN)

