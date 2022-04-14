class RNG:
    def __str__(self):
        return "Random Number Generator"
    
    @staticmethod
    def middle_square(n: int,seed: int, as_decimal: bool = False, include_seed: bool = False) -> list[int or float]:
        x0 = float(seed)/10000
        t_s, x_s = [seed], [x0]
        for i in range(n):
            t = str(t_s[i]**2)
            while len(t) < 8:
                t= list(t)
                t.insert(0,'0')
                t = ''.join(t)
            t = t[2:6]
            t_s.append(int(t))
            x = float(t)/10000
            x_s.append(x)
        if include_seed:
            if as_decimal:
                return x_s
            else:
                return t_s
        else:
            if as_decimal:
                return x_s[1:]
            else:
                return t_s[1:]

    
    @staticmethod
    def linear_congruence(n: int, a: int, b: int, c: int, seed: int) -> list[int]:
        x = [seed]
        for i in range(n):
            num = (a*x[i] + b) % c
            x.append(num)
        return x


