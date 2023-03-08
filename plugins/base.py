from abc import ABC, abstractproperty, abstractmethod


class Base(ABC):
    @abstractmethod
    def _get_full_data(self):
        ...

    @property
    def current(self):
        return self._get_full_data()

    @property
    @abstractproperty
    def draw_data(self):
        ...
