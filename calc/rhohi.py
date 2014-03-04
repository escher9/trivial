def rho(h):
    '''
    [MKS] SI unit
    find air density by passing h[km]

    example:

        if we know the height as 18[km]
        we can get rho by

        rho = rho(18)  

    '''
    return 1.2257 * (1- 0.0226*h) ** ( 4.25713 )
    # rho = 0.002378 * (1- 0.0226*h) ** ( 4.25713 )
    # return rho

print rho(18)
