from spookyMap.viewmodels.shared.viewmodelbase import ViewModelBase
from spookyMap.services import map_service


class RandomViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.ghosts_list = map_service.get_random_from_db()

