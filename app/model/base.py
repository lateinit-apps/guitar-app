from sqlalchemy.ext.declarative import declarative_base


class HumanReadable():

    __abstract__ = True

    def __repr__(self):
        package = self.__class__.__module__
        class_ = self.__class__.__name__
        key_values = sorted((c.name, getattr(self, c.name)) for c in self.__table__.columns)
        attributes = u', '.join(f'{x[0]}={repr(x[1])}' for x in key_values)
        return f'{package}.{class_}({attributes})'


Base = declarative_base(cls=HumanReadable)
