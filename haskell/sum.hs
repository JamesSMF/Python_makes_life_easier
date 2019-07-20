sumList     :: [Int] -> Int
sumList xs  =  if length xs == 1 then xs!!0
               else xs!!0 + sumList (tail xs)

sumList2        :: [Int] -> Int
sumList2 []     = 0
sumList2 [x]    = x
sumList2 (x:xs) = x + sumList2 xs
