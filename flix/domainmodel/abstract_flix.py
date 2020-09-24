from abc import ABC, abstractmethod, abstractproperty


class Flix(ABC):

    @property
    def name(self):
        raise NotImplementedError

    @property
    def information(self):
        '''
        This property store an introduction.
        Movie: director
        Actor: Actor of film <film> etc.
        Director: Director of film <film> etc.
        '''
        raise NotImplementedError

    @property
    def type(self):
        '''
        This property store a string of type:
        Movie, Actor, or Director
        '''
        raise NotImplementedError
