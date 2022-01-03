from spookyMap.viewmodels.shared.viewmodelbase import ViewModelBase

class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.bounds_ne = self.request_dict.bounds_ne
        self.bounds_sw = self.request_dict.bounds_sw
