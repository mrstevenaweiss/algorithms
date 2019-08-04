
class Primer( object ):
    def __init__( self ):
        """create a cache dictionary"""
        self.cache = {}

    def is_prime( self, x ):
        """Determine if x is prime, cache and return result"""
        if x in self.cache:
            return self.cache[x] # lookup result

        prime_flag = True

        if x == 1:
            prime_flag = False
        else:
            for i in range( 2, x ):
                if x % i == 0:
                    prime_flag = False
                    break

        self.cache[x] = prime_flag # cache result
        return prime_flag
