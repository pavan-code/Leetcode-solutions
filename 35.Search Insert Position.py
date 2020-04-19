def searchInsert ( nums, target ) :
        if target in nums :
                return nums .index ( target )
        else :
                nums. append( target )
                return sorted( nums ). index ( target )

nums = list ( map ( int, input (). split (',') ) )
target = int ( input () )
print ( searchInsert ( nums, target ) )
