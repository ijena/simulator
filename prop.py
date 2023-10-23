def non_negative(special_attr_name):
    # use special_attr_name from enclosing scope in definitions of fget/fset/fdel
    # define the fget/fset/fdel used to construct/returns a property object

    def get_non_negative(an_object):
        return getattr(an_object,special_attr_name)
        # same as return an_object.__dict__[special_attr_name]

    def set_non_negative(an_object, value):
        if  value < 0:
            raise ValueError(f'non_negative.set_non_negative: value({value}) not >= 0')
        setattr(an_object,special_attr_name, value)
        # same as an_object.__dict__[special_attr_name] = value

    def del_non_negative(an_object):
        delattr[an_object,special_attr_name]
        #same as del an_object.__dict__[special_attr_name])

    return property(get_non_negative, set_non_negative, del_non_negative)

class C:
    def __init__(self, c):
        self.c = c
    c=non_negative()

