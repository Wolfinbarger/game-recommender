class Platforms:
    """
        Args:
            **kwargs (str, optional): Expects any number of parameters with names that match a specific platform and
            whose value is a boolean indicating if the game is available on that platform. For any parameters missing,
            the default value is False.
        Example:
            platform = Platform(pc=False, ps4=True)
        """
    def __init__(self, **kwargs):
        self._pc = kwargs.get('pc', False)
        self._ps4 = kwargs.get('ps4', False)
        self._ps5 = kwargs.get('ps5', False)
        self._xbox_one_x = kwargs.get('xbox_one_x', False)
        self._nintendo_switch = kwargs.get('nintendo_switch', False)

    @property
    def pc(self):
        return self._pc

    @property
    def ps4(self):
        return self._ps4

    @property
    def ps5(self):
        return self._ps5

    @property
    def xbox_one_x(self):
        return self._xbox_one_x

    @property
    def nintendo_switch(self):
        return self._nintendo_switch

    def to_json(self):
        return {
            "pc": self.pc,
            "ps4": self.ps4,
            "ps5": self.ps5,
            "xbox_one_x": self.xbox_one_x,
            "nintendo_switch": self.nintendo_switch
        }
