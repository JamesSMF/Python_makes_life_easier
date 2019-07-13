-- get a list of divisors of x
divisors :: Int -> [Int]
divisors x = [d | d <- [2..x-1], x `mod` d == 0]

-- check if x and y have coprime
coprime :: Int -> Int -> Bool
coprime x y = disjoint (quicksort $ divisors x) (quicksort $ divisors y)

-- quick sort
quicksort :: [Int] -> [Int]
quicksort  []     =  []
quicksort  (x:xs) =  quicksort [y | y <- xs, y<x ] ++              -- recursion on left half
                     [x]                           ++              -- put the pivot here
                     quicksort [y | y <- xs, y>=x]                 -- recursion on right half

-- check if (xs AND ys) is empty (xs and ys should be sorted)
disjoint :: [Int] -> [Int] -> Bool
disjoint xs ys = if      length xs == 0 || length ys == 0 then True    -- comparison finishes: return True
                 else if xs!!0 == ys!!0 then False                     -- same divisor: return False
                 else if xs!!0 < ys!!0 then disjoint xs $ tail ys      -- recursion on ys' part
                 else disjoint ys $ tail xs                            -- recursion on xs' part

-- output all Pythagorean triads less than n
triads :: Int -> [(Int,Int,Int)]
triads n = [(x,y,z) | x <- [1..n], y <- [x+1..n], z <- [y+1..n], coprime x y, x*x + y*y == z*z]

